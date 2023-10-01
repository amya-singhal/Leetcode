class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String word: strs){
            char[] ar = word.toCharArray();
            Arrays.sort(ar);
            String wordSorted = new String(ar);
            if (!map.containsKey(wordSorted)){
                map.put(wordSorted, new ArrayList<>());
            }
            map.get(wordSorted).add(word);
        }
        return new ArrayList<>(map.values());
    }
}