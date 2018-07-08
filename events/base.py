import struct


class SerializableStruct:

    @classmethod
    def load(cls, data):
        return cls(*struct.unpack(cls.fmt, data))

    def dump(self):
        return struct.pack(
            self.fmt,
            *[getattr(self, attr) for attr in self.__slots__]
        )
