css = '''
<style>
.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex
}
.chat-message.user {
    background-color: #54548A
}
.chat-message.bot {
    background-color: #54548A
}
.chat-message .avatar {
  width: 20%;
  text-align: center;
}
.chat-message .avatar img {
  max-width: 40px;
  max-height: 40px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1rem;
  text-align: justify;
  font-style: italic;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.pinimg.com/564x/c7/3d/7f/c73d7fdfee9c085412e751bbe855c050.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

#bot  style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;"
user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.pinimg.com/564x/b2/f9/13/b2f913b11d03d2d7b47702f42ae2cdac.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''