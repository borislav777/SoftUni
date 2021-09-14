class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = input()
emai = []
while not emails == "Stop":
    sender, receiver, content = emails.split()
    email = Email(sender, receiver, content)
    emai.append(email)
    emails = input()

indices = [int(index) for index in input().split(", ")]
for ind in indices:
    emai[ind].send()

for email in emai:
    print(email.get_info())
