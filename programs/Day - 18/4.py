# Abstract Class as an Interface
# Instructions:
# Create an abstract class named Notification with abstract method:
# send_message().
# Create concrete classes:
# EmailNotification
# SMSNotification
# PushNotification
# Create instances of each class and call send_message() in a loo

from abc import ABC, abstractmethod
class Notification(ABC):
    
    @abstractmethod
    def send_message(self):
        pass

class Email_Notification(Notification):
    def send_message(self):
        print("Sending Email Notification")

class SMS_Notification(Notification):
    def send_message(self):
        print("Sending SMS Notification")

class Push_Notification(Notification):
    def send_message(self):
        print("Sending Push Notification")

notifications = [ Email_Notification(),SMS_Notification(),Push_Notification()]

for i in notifications:
    i.send_message()