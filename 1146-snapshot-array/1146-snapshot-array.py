class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = []
        self.array = dict()
        self.changed = True
        

    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        self.changed = True
        

    def snap(self) -> int:
        if self.changed:
            self.snapshots.append({**self.array})
        else:
            self.snapshots.append(self.snapshots[-1])
        self.changed = False
        return len(self.snapshots) - 1
        

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id].get(index, 0)
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)