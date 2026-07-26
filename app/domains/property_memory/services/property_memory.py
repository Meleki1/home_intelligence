
class PropertyMemoryService:
    def __init__(self):
        self.memories = {}

    async def add_memory(self, home_id, memory):
        if home_id not in self.memories:
            self.memories[home_id] = []

        self.memories[home_id].append(
            memory
        )


    async def get_memories(self, home_id):
        return self.memories.get(
            home_id,
            []
        )