import re
sentence='''Aaronson was born on 18 February 1895[note 1] at 34 Great Pearl Street, Spitalfields in the East End of London to poor Orthodox Jewish parents who had immigrated from Vilna in the Pale of Settlement in Eastern Europe.[1][2] His father was Louis Aaronson, a bootmaker, and his mother was Sarah Aaronson, née Kowalski. He attended Whitechapel City Boys' School and later received a scholarship to attend Hackney Downs grammar school.[1]

His father emigrated to New York in 1905. The rest of the family followed in 1912, except for 17-year old Lazarus who remained in London. From then on, he lived with the family of Joseph Posener at 292 Commercial Road in the East End of London. At the time, the area was a hub of the Jewish diaspora and at the turn of the 20th century, a quarter of its population were Jews from Central and Eastern Europe. Growing up in the East End, Aaronson was part of a group of friends who are today referred to as the Whitechapel Boys, all of whom were children of Jewish immigrants and shared literary and artistic ambitions.[3] Others in the group who, like Aaronson, later achieved distinction included John Rodker, Isaac Rosenberg, Joseph Leftwich, Samuel Winsten, Clara Birnberg, David Bomberg, and the brothers Abraham and Joseph Fineberg.[4] Aaronson was also involved in the Young Socialist League, where he and other Whitechapel Boys helped organise educational meetings on modern art and radical politics.[5] Aaronson remained a committed socialist throughout adulthood.[6]

The Stake
All that I am is staked on words.
Bless their meaning, Lord, or I become
Slave to the heavy, hollow, mindless drum.

Make me the maker of my words.
Let me renew myself in my own speech,
Till I become at last the thing I teach.

And let a taste be in my words,
That men may savour what is man in me,
And know how much I fail, how little see.

Let not my pleasure in my words
Forget the silence whence all speech has sprung,
The cell and meditation of the tongue.

And at the end, the Word of words,
Lord! make my dedication. Let me live
Towards Your patient love that can forgive

The blasphemy and pride of words
Since once You spoke. Your praise is there.
I mean it thus, even in my despair.

—The Homeward Journey and Other Poems, 1946
Having been diagnosed with tuberculosis and diabetes, Aaronson did not serve in the military during the First World War. Between 1913 and 1915, and again between 1926 and 1928, he studied economics with a special focus on public administration at the London School of Economics, but never completed his degree.[1][7]'''
print(sentence)

pattern=re.compile(r'\d\d')
matches=pattern.finditer(sentence)
for j in matches:
    print(j)
