package Medium.AddTwoNumbers;

public class LongestSubstring {

    public static void main(String args[]){
        String s = "aabaab!bb";
        System.out.println(lengthOfLongestSubstring(s));
    }

    public static int lengthOfLongestSubstring(String s) {
        int max=s.length() > 0 ? 1 : 0 ;
        int count = 1;
        String res = s.length() > 0 ? String.valueOf(s.charAt(0)) : "";
        for(int i = 1; i<s.length();i++){
            if(!res.contains(String.valueOf(s.charAt(i)))){
                count++;
                max = Math.max(count, max);
            }else{
                max = Math.max(count,max);
                res = res.substring(res.indexOf(s.charAt(i))+1);
                count = res.length()+1;
            }
            res += String.valueOf(s.charAt(i));
        }
        return max;
    }
}





