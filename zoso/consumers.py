import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat, ChatRoom
# https://channels.readthedocs.io/en/latest/topics/consumers.html

class ChatConsumer(AsyncWebsocketConsumer):
	# Set roomname and groupname when connecting to Websocket
	async def connect(self):
		# Roomname and Groupname
		self.roomname = self.scope['url_route']['kwargs']['roomname']
		self.room_group_name = 'chat_%s' % self.roomname

		# Join the room group
		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
		)

		# Called on connection.
        # To accept the connection call
		await self.accept()



	# Handle the disconnect
	async def disconnect(self, close_code):
		# Leave room group
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
		)


	# Handle receiving message from Websocket
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']
		self.user_id = self.scope['user'].id

		# Find chatroom object
		chatroomname = await database_sync_to_async(ChatRoom.objects.get)(roomname=self.roomname)

		# Create new chat object
		chat = Chat(
			chattext=message,
			user=self.scope['user'],
			roomname=chatroomname
		)

		# Save the chat to the databsea
		await database_sync_to_async(chat.save)()

		# Send the message to the room group
		await self.channel_layer.group_send(
			self.room_group_name,
			{
				'type': 'chat_message',
				'message': message,
				'user_id': self.user_id
			})



	# Handle receive message from room group
	async def chat_message(self, event):
		message = event['message']
		user_id = event['user_id']

		# Send message and user id to Websocket
		await self.send(text_data=json.dumps({
			'message': message,
			'user_id': user_id
		}))