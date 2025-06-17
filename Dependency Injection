class EmailService:
    def send(self, message):
        print("Email sent:", message)

class Notification:
    def __init__(self, service):
        self.service = service

    def notify(self, message):
        self.service.send(message)

# Penggunaan
email = EmailService()
notif = Notification(email)
notif.notify("Hello from DIP!")
