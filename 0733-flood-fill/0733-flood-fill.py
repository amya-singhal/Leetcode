class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        prev = image[sr][sc]
        if (prev == color):
            return image
        m = len(image)
        n = len(image[0])
        def recur (image, sr, sc):
            image[sr][sc] = color
            if (sr - 1 >= 0 and image[sr-1][sc] == prev):
                recur(image, sr-1, sc)
            if (sc - 1 >= 0 and image[sr][sc-1] == prev):
                recur(image, sr, sc-1)
            if (sr + 1 < m and image[sr+1][sc] == prev):
                recur(image, sr+1, sc)
            if (sc+1 < n and image[sr][sc+1] == prev):
                recur(image, sr, sc+1)
            return
        recur(image, sr, sc)
        return image
        