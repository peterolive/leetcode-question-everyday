import heapq


class MyCalendarThree:

    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> int:
        self.books.append((start, end))
        self.books = sorted(self.books, key=lambda x: x[1])

        heap = []
        heapq.heappush(heap, self.books[0][1])

        for i in range(1, len(self.books)):
            if self.books[i][0] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, self.books[i][1])
            else:
                heapq.heappush(heap, self.books[i][1])

        return len(heap)
