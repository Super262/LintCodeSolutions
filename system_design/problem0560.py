class FriendshipService:

    def __init__(self):
        self.followers = {}
        self.followings = {}

    """
    @param: user_id: An integer
    @return: all followers and sorting by user_id
    """

    def getFollowers(self, user_id: int) -> list:
        if user_id not in self.followers:
            return []
        results = list(self.followers[user_id])
        results.sort()
        return results

    """
    @param: user_id: An integer
    @return: all followings and sorting by user_id
    """

    def getFollowings(self, user_id: int) -> list:
        if user_id not in self.followings:
            return []
        results = list(self.followings[user_id])
        results.sort()
        return results

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def follow(self, to_user_id: int, from_user_id: int) -> None:
        if to_user_id not in self.followers:
            self.followers[to_user_id] = set()
        if from_user_id not in self.followings:
            self.followings[from_user_id] = set()
        self.followers[to_user_id].push(from_user_id)
        self.followings[from_user_id].push(to_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def unfollow(self, to_user_id: int, from_user_id: int) -> None:
        if from_user_id in self.followings:
            if to_user_id in self.followings[from_user_id]:
                self.followings[from_user_id].remove(to_user_id)
        if to_user_id in self.followers:
            if from_user_id in self.followers[to_user_id]:
                self.followers[to_user_id].remove(from_user_id)
