# 对应leetcode 389

'''
    给定两个字符串s和t，只包含小写字母；
    字符串t由字符串s随机重排，然后在随机位置添加一个字母；
    要找到在t中被添加的字母。
'''

from typing import List,Dict

class Solution:
    def __init__(self):
        self.hashtable_s = {}
        self.hashtable_t = {}
        self.key_s_list = []
        self.key_t_list = []
        self.value_s_list = []
        self.value_t_list = []
    
    def findTheDifference(self,s:str,t:str):
        for c1 in s:
            if c1 in self.hashtable_s:
                self.hashtable_s[c1] = self.hashtable_s.get(c1,0) + 1
            else:
                self.hashtable_s[c1] = 1
        for c2 in t:
            if c2 in self.hashtable_t:
                self.hashtable_t[c2] = self.hashtable_t.get(c2,0) + 1
            else:
                self.hashtable_t[c2] = 1
        for key,value in self.hashtable_s.items():
            self.key_s_list.append(key)
            self.value_s_list.append(value) 
        for key,value in self.hashtable_t.items():
            self.key_t_list.append(key)
            self.value_t_list.append(value)

        if self.key_s_list != self.key_t_list:
            x = [x for x in self.key_t_list if x not in self.key_s_list]
            print(len(x))
            print(x)
            print(x[0])
            return x[0]
        else:
            print(self.value_s_list)
            print(self.value_t_list)
            y = [y for y in self.value_t_list if y not in self.value_s_list]
            print(type(y)) # list
            for key in self.key_t_list:
                print(type(key))
                if self.hashtable_t.get(key) == y[0]:
                    print(key)
                    return key
        
        
if __name__ == "__main__":
    test = Solution()
    test.findTheDifference("ymbgaraibkfmvocpizdydugvalagaivdbfsfbepeyccqfepzvtpyxtbadkhmwmoswrcxnargtlswqemafandgkmydtimuzvjwxvlfwlhvkrgcsithaqlcvrihrwqkpjdhgfgreqoxzfvhjzojhghfwbvpfzectwwhexthbsndovxejsntmjihchaotbgcysfdaojkjldprwyrnischrgmtvjcorypvopfmegizfkvudubnejzfqffvgdoxohuinkyygbdzmshvyqyhsozwvlhevfepdvafgkqpkmcsikfyxczcovrmwqxxbnhfzcjjcpgzjjfateajnnvlbwhyppdleahgaypxidkpwmfqwqyofwdqgxhjaxvyrzupfwesmxbjszolgwqvfiozofncbohduqgiswuiyddmwlwubetyaummenkdfptjczxemryuotrrymrfdxtrebpbjtpnuhsbnovhectpjhfhahbqrfbyxggobsweefcwxpqsspyssrmdhuelkkvyjxswjwofngpwfxvknkjviiavorwyfzlnktmfwxkvwkrwdcxjfzikdyswsuxegmhtnxjraqrdchaauazfhtklxsksbhwgjphgbasfnlwqwukprgvihntsyymdrfovaszjywuqygpvjtvlsvvqbvzsmgweiayhlubnbsitvfxawhfmfiatxvqrcwjshvovxknnxnyyfexqycrlyksderlqarqhkxyaqwlwoqcribumrqjtelhwdvaiysgjlvksrfvjlcaiwrirtkkxbwgicyhvakxgdjwnwmubkiazdjkfmotglclqndqjxethoutvjchjbkoasnnfbgrnycucfpeovruguzumgmgddqwjgdvaujhyqsqtoexmnfuluaqbxoofvotvfoiexbnprrxptchmlctzgqtkivsilwgwgvpidpvasurraqfkcmxhdapjrlrnkbklwkrvoaziznlpor"
,"qhxepbshlrhoecdaodgpousbzfcqjxulatciapuftffahhlmxbufgjuxstfjvljybfxnenlacmjqoymvamphpxnolwijwcecgwbcjhgdybfffwoygikvoecdggplfohemfypxfsvdrseyhmvkoovxhdvoavsqqbrsqrkqhbtmgwaurgisloqjixfwfvwtszcxwktkwesaxsmhsvlitegrlzkvfqoiiwxbzskzoewbkxtphapavbyvhzvgrrfriddnsrftfowhdanvhjvurhljmpxvpddxmzfgwwpkjrfgqptrmumoemhfpojnxzwlrxkcafvbhlwrapubhveattfifsmiounhqusvhywnxhwrgamgnesxmzliyzisqrwvkiyderyotxhwspqrrkeczjysfujvovsfcfouykcqyjoobfdgnlswfzjmyucaxuaslzwfnetekymrwbvponiaojdqnbmboldvvitamntwnyaeppjaohwkrisrlrgwcjqqgxeqerjrbapfzurcwxhcwzugcgnirkkrxdthtbmdqgvqxilllrsbwjhwqszrjtzyetwubdrlyakzxcveufvhqugyawvkivwonvmrgnchkzdysngqdibhkyboyftxcvvjoggecjsajbuqkjjxfvynrjsnvtfvgpgveycxidhhfauvjovmnbqgoxsafknluyimkczykwdgvqwlvvgdmufxdypwnajkncoynqticfetcdafvtqszuwfmrdggifokwmkgzuxnhncmnsstffqpqbplypapctctfhqpihavligbrutxmmygiyaklqtakdidvnvrjfteazeqmbgklrgrorudayokxptswwkcircwuhcavhdparjfkjypkyxhbgwxbkvpvrtzjaetahmxevmkhdfyidhrdeejapfbafwmdqjqszwnwzgclitdhlnkaiyldwkwwzvhyorgbysyjbxsspnjdewjxbhpsvj")

# 上述是自己写的，感觉有点垃圾
    