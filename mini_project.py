class VirtualMemory:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = []
        self.page_faults = 0

    def fifo(self, reference_string):
        self.frames = []
        self.page_faults = 0

        for page in reference_string:
            if page not in self.frames:
                if len(self.frames) < self.num_frames:
                    self.frames.append(page)
                else:
                    self.frames.pop(0)
                    self.frames.append(page)
                self.page_faults += 1
        return self.page_faults

    def lru(self, reference_string):
        self.frames = []
        self.page_faults = 0
        lru_dict = {}

        for i, page in enumerate(reference_string):
            if page not in self.frames:
                if len(self.frames) < self.num_frames:
                    self.frames.append(page)
                else:
                    
                    lru_page = min(lru_dict, key=lru_dict.get)
                    self.frames.remove(lru_page)
                    self.frames.append(page)
                    del lru_dict[lru_page]
                self.page_faults += 1
            lru_dict[page] = i
        return self.page_faults



num_frames = int(input("Enter the number of page frames: "))
reference_string = list(map(int, input("Enter the reference string (space-separated values): ").split()))

vm = VirtualMemory(num_frames)


fifo_page_faults = vm.fifo(reference_string)
lru_page_faults = vm.lru(reference_string)


print(f"\nReference String: {reference_string}")
print(f"Number of Frames: {num_frames}")
print(f"FIFO Page Faults: {fifo_page_faults}")
print(f"LRU Page Faults: {lru_page_faults}")
