class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score


class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results: list) -> dict:
        id_to_heap = dict()
        import heapq
        for item in results:
            if item.id not in id_to_heap:
                id_to_heap[item.id] = []
            heapq.heappush(id_to_heap[item.id], item.score)
            if len(id_to_heap[item.id]) > 5:
                heapq.heappop(id_to_heap[item.id])
        avg_scores = dict()
        for id in id_to_heap:
            avg_scores[id] = sum(id_to_heap[id]) / 5
        return avg_scores
