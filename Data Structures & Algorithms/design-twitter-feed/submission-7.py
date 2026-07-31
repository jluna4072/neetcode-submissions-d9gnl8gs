class Twitter:
    '''
    3 structures:
    user_folowing -> dict representing who the user is following, simple list of userIds
    user_following -> dict holding more dicts, userId -> followerId: index in user_following list
    user_tweets -> holds a list of the user tweets
    '''
    def __init__(self):
        self.user_following = defaultdict(list)
        self.user_tweets = defaultdict(list)
        self.user_following_index = defaultdict(lambda: defaultdict(int))
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        time = self.time
        self.user_tweets[userId].append((time, tweetId))
        self.time+= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [] + self.user_tweets[userId]

        for followee in self.user_following[userId]:
            heap+= self.user_tweets[followee]

        heapq.heapify_max(heap)
        res = []
        
        for _ in range(min(10,len(heap))):
            res.append(heapq.heappop_max(heap)[1])
        
        return res




    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId in self.user_following[followerId]:
            return
        self.user_following[followerId].append(followeeId)
        i = len(self.user_following[followerId]) - 1
        self.user_following_index[followerId][followerId] = i

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.user_following[followerId]:
            return
        temp = self.user_following_index[followerId][followeeId]
        self.user_following[followerId][temp], self.user_following[followerId][-1] = self.user_following[followerId][-1], self.user_following[followerId][temp]
        self.user_following[followerId].pop()
        del self.user_following_index[followerId][followeeId]
