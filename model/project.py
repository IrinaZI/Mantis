from sys import maxsize

class Project:
    def __init__(self, name=None, status=None, inherit_global=None, view_status=None, description=None, id = None):
        self.Name = name
        self.Status = status
        self.Inherit_global = inherit_global
        self.View_status = view_status
        self.Description=description
        self.Id = id
    def __repr__(self):
        return "%s:%s;%s;%s" % (self.Id, self.Name, self.Status, self.View_status)
    def __eq__(self, other):
        return (self.Id is None or other.id is None or self.Id == other.id) and self.Name == other.name

    def id_or_max(self):
        if self.Id:
            return int(self.Id)
        else:
            return maxsize