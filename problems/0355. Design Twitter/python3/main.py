from typing import List
import heapq

RECENT_TWEETS_COUNT = 10


class User:
    def __init__(self, id):
        self.id = id
        # for the purposes of this problem,
        # all users are considered to be following themselves
        self.followers = set([id])
        self.following = set([id])
        self.news_feed = []
        self.posts = []

    def post(self, tick, tweetId):
        heapq.heappush(self.posts, (tick, self.id, tweetId))

    def add_to_news_feed(self, tick, authorId, tweetId):
        if authorId == self.id:
            self.post(tick, tweetId)

        heapq.heappush(self.news_feed, (tick, authorId, tweetId))

    def get_news_feed(self):
        newest = heapq.nlargest(RECENT_TWEETS_COUNT, self.news_feed)

        # we're only interested in the tweetId
        return [news[2] for news in newest]

    def unfollow(self, userId):
        # delete all the user's items from the news feed
        # expensive if we are to repeatedly unfollow / follow the same user
        # generally, I'm okay with unfollow() being slow for get_news_feed() to be fast
        new_feed = []
        for item in self.news_feed:
            if item[1] != userId:
                heapq.heappush(new_feed, item)

        self.news_feed = new_feed

        if userId in self.following:
            self.following.remove(userId)

    def follow(self, other):
        self.following.add(other.id)

        for post in other.posts:
            self.add_to_news_feed(*post)


class Twitter:
    def __init__(self):
        self.tick = 0
        self.users: dict[int, User] = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)

        self.tick += 1

        if userId not in self.users:
            user = User(userId)
            self.users[userId] = user

        user = self.users[userId]
        followers = user.followers

        for followerId in list(followers):
            follower = self.users[followerId]
            follower.add_to_news_feed(self.tick, userId, tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.users[userId] = User(userId)
        return self.users[userId].get_news_feed()

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            user = User(followerId)
            self.users[followerId] = user
        if followeeId not in self.users:
            user = User(followeeId)
            self.users[followeeId] = user

        follower, followee = self.users[followerId], self.users[followeeId]

        if followeeId in follower.following:
            return

        follower.follow(followee)
        followee.followers.add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        follower, followee = self.users[followerId], self.users[followeeId]

        if followeeId not in follower.following:
            return

        follower.unfollow(followeeId)
        if followerId in followee.followers:
            followee.followers.remove(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


if __name__ == "__main__":
    # t = Twitter()
    # t.postTweet(1, 5)
    # assert t.getNewsFeed(1) == [5]
    # t.follow(1, 2)
    # t.postTweet(2, 6)
    # assert t.getNewsFeed(1) == [6, 5]
    # t.unfollow(1, 2)
    # assert t.getNewsFeed(1) == [5]

    t = Twitter()
    t.follow(1, 2)
    t.postTweet(2, 5)
    t.postTweet(2, 6)
    t.postTweet(1, 10)
    t.postTweet(2, 7)
    assert t.getNewsFeed(1) == [7, 10, 6, 5]
    t.unfollow(1, 2)
    assert t.getNewsFeed(1) == [10]
    t.follow(1, 2)
    assert t.getNewsFeed(1) == [7, 10, 6, 5]
