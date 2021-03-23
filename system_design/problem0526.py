class LoadBalancer:
    def __init__(self):
        self.servers = []
        self.server_to_index = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """

    def add(self, server_id: int) -> None:
        self.server_to_index[server_id] = len(self.servers)
        self.servers.append(server_id)

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """

    def remove(self, server_id: int) -> None:
        if server_id in self.server_to_index:
            removed_index = self.server_to_index[server_id]
            tail_index = len(self.servers) - 1
            tail_id = self.servers[tail_index]
            self.servers[removed_index], self.servers[tail_index] = self.servers[tail_index], self.servers[
                removed_index]
            self.server_to_index.pop(server_id)
            self.server_to_index[tail_id] = removed_index
            self.servers.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """

    def pick(self) -> int:
        if not self.servers:
            return -1
        import random
        return self.servers[random.randrange(0, len(self.servers))]
