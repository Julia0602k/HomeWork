class KeyboardButton:

    def __init__(self, text: str, request_contact: bool, request_location: bool):
        if not isinstance(text, str):
            raise TypeError('text must be str')
        if not isinstance(request_contact, bool):
            raise TypeError('request_contact must be bool')
        if not isinstance(request_location, bool):
            raise TypeError('request_location must be bool')
        if request_contact and request_location:
            raise ValueError
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location

    def dict(self):
        return {'text': self.text, 'request_contact': self.request_contact, 'request_location': self.request_location}