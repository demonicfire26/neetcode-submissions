class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        delimeter = "|"
        for i in strs:
            len_str = len(i)
            encoded_str = encoded_str+str(len_str)+delimeter+i
        return encoded_str


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            delim_pos = s.find("|",i)
            length = int(s[i:delim_pos])
            string_start = delim_pos+1
            string_end = string_start+length
            decode = s[string_start:string_end]

            result.append(decode)
            
            i = string_end

        return result

