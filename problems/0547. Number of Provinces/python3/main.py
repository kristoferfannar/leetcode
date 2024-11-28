from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces: dict[int, list] = dict()
        belongs: dict[int, int] = dict()

        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected[i])):
                # print(f"\nprovinces: {provinces}")
                # print(f"belongs: {belongs}")
                if isConnected[i][j]:
                    # extend j's province into i's province
                    if i in belongs and j in belongs:
                        if belongs[i] == belongs[j]:
                            continue

                        # print(f"i-{i} j-{j}: i & j belong")
                        provinces[belongs[i]].extend(provinces[belongs[j]])

                        for num in provinces[belongs[j]]:
                            if num != j:
                                belongs[num] = belongs[i]

                        del provinces[belongs[j]]
                        belongs[j] = belongs[i]

                        # print(f"provinces[{belongs[i]}] = {provinces[belongs[i]]}")

                    elif i in belongs:
                        # print(f"i-{i} j-{j}: i belongs")
                        belongs[j] = belongs[i]
                        provinces[belongs[i]].append(j)
                        # print(f"provinces[{belongs[i]}] = {provinces[belongs[i]]}")

                    elif j in belongs:
                        # print(f"i-{i} j-{j}: j belongs")
                        belongs[i] = belongs[j]
                        provinces[belongs[i]].append(i)
                        # print(f"provinces[{belongs[i]}] = {provinces[belongs[i]]}")

                    else:
                        # print(f"i-{i} j-{j}: neither belong")
                        belongs[j] = i
                        belongs[i] = i
                        provinces[i] = [i, j]
                        # print(f"provinces[{belongs[i]}] = {provinces[belongs[i]]}")

        grouped = 0
        for prov, items in provinces.items():
            grouped += len(items)
            # print(f"{prov}: {items}")

        # print(
        #     f"len(provinces) = {len(provinces)}, len(isConnected) = {len(isConnected)}, grouped = {grouped}"
        # )
        return len(provinces) + len(isConnected) - grouped


if __name__ == "__main__":
    # 1 1 0
    # 1 1 0
    # 0 0 1
    # assert Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2

    # 1 0 0 1
    # 0 1 1 0
    # 0 1 1 1
    # 1 0 1 1

    # 0: [0, 3]
    # 1: [1, 2]
    # assert (
    #     Solution().findCircleNum(
    #         [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    #     )
    #     == 1
    # )

    # assert Solution().findCircleNum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 1

    assert (
        Solution().findCircleNum(
            [
                [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            ]
        )
        == 3
    )
