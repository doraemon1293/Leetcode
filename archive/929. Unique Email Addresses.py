class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails=set()
        for email in emails:
            s=email.split("@")[0]
            s=s.split("+")[0]
            s=s.replace(".","")
            s=s+"@"+email.split("@")[1]
            unique_emails.add(s)
        return len(unique_emails)