class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res_list = []
        for i in emails:
            str_stamp = i[:i.find('+')]
            str_stamp = str_stamp.replace('.', '')
            str_stamp += i[i.find('@'):]
            res_list.append(str_stamp)
        return len(set(res_list))
