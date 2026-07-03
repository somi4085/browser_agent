class AgentMemory:

    def __init__(self):
        self.steps = []
        self.errors = []

    def add_step(self, action:str, result:str, success:bool):
        self.steps.append({
            "action":action,
            "result":result,
            "success":success
        })

    def add_error(self, error:str):
        self.errors.append({
            "error": error
        })
    def get_history(self):

        return self.steps[-5:]