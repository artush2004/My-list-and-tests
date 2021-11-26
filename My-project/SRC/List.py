class my_list():
    def __init__(self, *args):
        self._mylist = [el for el in args]

    def __repr__(self):
        return str(self._mylist)

    def __len__(self):
        return len(self._mylist)

    def __getitem__(self, item):
        try:
            return self._mylist[item]
        except:
            "index not found"

    def __setitem__(self, key, value):
        try:
            self._mylist[key] = value
        except:
            "index not found"

    def __reversed__(self):
        return self._mylist.reverse()

    def pop(self, index=-1):
        try:
            return self._mylist.pop(index)
        except:
            "index not found"

    def append(self, value):
        self._mylist.append(value)
