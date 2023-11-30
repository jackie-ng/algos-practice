class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # decrement for the next tweets (keep track of the most recent tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        # Retrieve the 10 most recent tweet ids in the user's news feed. 
        # Each item in the news feed must be posted by users who the user followed or by the user herself. 
        # Tweets must be ordered from most recent to least recent.
        
        # 1. res will store the result, i.e., the list of tweet IDs in the user's news feed. 
        # minHeap is a min-heap that will be used to efficiently retrieve the most recent tweets.
        res = []
        minHeap = []
        
        # 2. Adding the user to their own followees
        # This ensures that the user's own tweets will be included in their news feed.
        self.followMap[userId].add(userId)
        
        # 3. Populating the min heap with initial tweets
        # It iterates through the users that the specified user is following (followee) 
        # and pushes their latest tweets onto the min heap. 
        # Each element in the heap is a list [count, tweetId, followeeId, index], 
        # count: timestamp, tweetId: ID of the tweet, followeeId: ID of the user who posted the tweet, 
        # index: index of the tweet in the user's tweet list.
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 # last value of the list
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1]) # index - 1 for next tweet

        # 4. Retrieving the 10 most recent tweets from the min heap
        # It pops elements from the min heap (which are the tweets with the smallest timestamps) and appends the tweet ID to the result list. If there are more tweets from the same user, they are pushed onto the heap for further consideration.
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
