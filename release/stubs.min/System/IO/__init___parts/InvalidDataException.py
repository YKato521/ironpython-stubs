class InvalidDataException(SystemException, ISerializable, _Exception):
    """
 The exception that is thrown when a data stream is in an invalid format.

 

 InvalidDataException()

 InvalidDataException(message: str)

 InvalidDataException(message: str,innerException: Exception)
 """

    def add_SerializeObjectState(self, *args):
        """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args):
        """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args):
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod
    def __new__(self, message=None, innerException=None):
        """
  __new__(cls: type)

  __new__(cls: type,message: str)

  __new__(cls: type,message: str,innerException: Exception)
  """
        pass

    def __reduce_ex__(self, *args):
        pass

    def __str__(self, *args):
        pass
