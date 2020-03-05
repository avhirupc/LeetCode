"""Approach 1: Wrong submission for dvdf"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_slen,current_maxlen=0,0
        st_ptr,en_ptr=0,0
        char_in_max_ss=[]
        while(en_ptr<len(s)):
            if s[en_ptr] not in char_in_max_ss:
                current_maxlen+=1
                char_in_max_ss.append(s[en_ptr])
                en_ptr+=1
            else:
                if current_maxlen>max_slen:
                    max_slen=current_maxlen
                current_maxlen=1
                st_ptr=en_ptr
                en_ptr+=1
                char_in_max_ss=[s[st_ptr]]
        if current_maxlen>max_slen:
            return current_maxlen
        return max_slen

"""Approach 2: Wrong submission at abcabcaa"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_slen=0
        st_ptr,en_ptr=0,0
        char_in_max_ss=set()
        while(en_ptr<len(s)):
            if s[en_ptr] not in char_in_max_ss:
                char_in_max_ss.add(s[en_ptr])
                en_ptr+=1
            else:
                if (en_ptr-st_ptr)>max_slen:
                    max_slen=(en_ptr-st_ptr)
                while(s[en_ptr] in char_in_max_ss):
                    char_in_max_ss.remove(s[st_ptr])
                    st_ptr+=1
        if en_ptr-st_ptr>max_slen:
            return en_ptr-st_ptr
        return max_slen