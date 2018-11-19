class Admin(Moderator):
    """Admin class"""
    def __init__(self):
        super()

    def can_edit(self):
        return True

    def can_delete(self):
        return True


