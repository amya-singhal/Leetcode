class Solution {
    public void helper(int[] candidates, int target, List<List<Integer>> answer, int index, List<Integer> tmpArray){
        if (index == -1){
            if (target == 0){
                answer.add(new ArrayList<>(tmpArray));
            }
            return;
        }
        if (target < 0)
            return;
        if (target == 0) {
            answer.add(new ArrayList<>(tmpArray));
            return;
        }
        tmpArray.add(candidates[index]);
        helper(candidates, target-candidates[index], answer, index, tmpArray);
        tmpArray.remove(tmpArray.size() - 1);
        helper(candidates, target, answer, index-1, tmpArray);
        return;
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> answer = new ArrayList<>();
        int n = candidates.length;
        helper(candidates, target, answer, n-1, new ArrayList<>());
        return answer;
    }
}