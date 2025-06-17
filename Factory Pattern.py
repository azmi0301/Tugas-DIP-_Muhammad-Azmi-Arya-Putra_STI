class EmailService:
    def send(self, msg):
        print("Email:", msg)

class SMSService:
    def send(self, msg):
        print("SMS:", msg)

class ServiceFactory:
    @staticmethod
    def create_service(type):
        if type == "email":
            return EmailService()
        elif type == "sms":
            return SMSService()

# Penggunaan
service = ServiceFactory.create_service("sms")
service.send("Hello via SMS")
