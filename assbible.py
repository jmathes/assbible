import webapp2
import jinja2
import os
import random
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


ass_list = {
    'DEUTERONOMY 22:10': 'Thou shalt not plow with an ox and an ass together.',
    'DEUTERONOMY 22:3': "In like manner shalt thou do with his ass; and so shalt thou do with his raiment; and with all lost thing of thy brother's, which he hath lost, and thou hast found, shalt thou do likewise: thou mayest not hide thyself.",
    'DEUTERONOMY 22:4': "Thou shalt not see thy brother's ass or his ox fall down by the way, and hide thyself from them: thou shalt surely help him to lift them up again.",
    'DEUTERONOMY 28:31': 'Thine ox shall be slain before thine eyes, and thou shalt not eat thereof: thine ass shall be violently taken away from before thy face, and shall not be restored to thee: thy sheep shall be given unto thine enemies, and thou shalt have none to rescue them.',
    'DEUTERONOMY 5:14': 'But the seventh day is the sabbath of the LORD thy God: in it thou shalt not do any work, thou, nor thy son, nor thy daughter, nor thy manservant, nor thy maidservant, nor thine ox, nor thine ass, nor any of thy cattle, nor thy stranger that is within thy gates; that thy manservant and thy maidservant may rest as well as thou.',
    'DEUTERONOMY 5:21': "Neither shalt thou desire thy neighbour's wife, neither shalt thou covet thy neighbour's house, his field, or his manservant, or his maidservant, his ox, or his ass, or any thing that is thy neighbour's.",
    'EXODUS 13:13': 'And every firstling of an ass thou shalt redeem with a lamb; and if thou wilt not redeem it, then thou shalt break his neck: and all the firstborn of man among thy children shalt thou redeem.',
    'EXODUS 20:17': "Thou shalt not covet thy neighbour's house, thou shalt not covet thy neighbour's wife, nor his manservant, nor his maidservant, nor his ox, nor his ass, nor any thing that is thy neighbour's.",
    'EXODUS 21:33': 'And if a man shall open a pit, or if a man shall dig a pit, and not cover it, and an ox or an ass fall therein;',
    'EXODUS 22:10': 'If a man deliver unto his neighbour an ass, or an ox, or a sheep, or any beast, to keep; and it die, or be hurt, or driven away, no man seeing it:',
    'EXODUS 22:4': 'If the theft be certainly found in his hand alive, whether it be ox, or ass, or sheep; he shall restore double.',
    'EXODUS 22:9': 'For all manner of trespass, whether it be for ox, for ass, for sheep, for raiment, or for any manner of lost thing, which another challengeth to be his, the cause of both parties shall come before the judges; and whom the judges shall condemn, he shall pay double unto his neighbour.',
    'EXODUS 23:12': 'Six days thou shalt do thy work, and on the seventh day thou shalt rest: that thine ox and thine ass may rest, and the son of thy handmaid, and the stranger, may be refreshed.',
    'EXODUS 23:4': "If thou meet thine enemy's ox or his ass going astray, thou shalt surely bring it back to him again.",
    'EXODUS 23:5': 'If thou see the ass of him that hateth thee lying under his burden, and wouldest forbear to help him, thou shalt surely help with him.',
    'EXODUS 34:20': 'But the firstling of an ass thou shalt redeem with a lamb: and if thou redeem him not, then shalt thou break his neck.  All the firstborn of thy sons thou shalt redeem.  And none shall appear before me empty.',
    'EXODUS 4:20': 'And Moses took his wife and his sons, and set them upon an ass, and he returned to the land of Egypt: and Moses took the rod of God in his hand.',
    'FIRST KINGS 13:13': 'And he said unto his sons, Saddle me the ass.  So they saddled him the ass: and he rode thereon,',
    'FIRST KINGS 13:23': 'And it came to pass, after he had eaten bread, and after he had drunk, that he saddled for him the ass, to wit, for the prophet whom he had brought back.',
    'FIRST KINGS 13:24': 'And when he was gone, a lion met him by the way, and slew him: and his carcase was cast in the way, and the ass stood by it, the lion also stood by the carcase.',
    'FIRST KINGS 13:27': 'And he spake to his sons, saying, Saddle me the ass.  And they saddled him.',
    'FIRST KINGS 13:28': 'And he went and found his carcase cast in the way, and the ass and the lion standing by the carcase: the lion had not eaten the carcase, nor torn the ass.',
    'FIRST KINGS 13:29': 'And the prophet took up the carcase of the man of God, and laid it upon the ass, and brought it back: and the old prophet came to the city, to mourn and to bury him.',
    'FIRST KINGS 2:40': 'And Shimei arose, and saddled his ass, and went to Gath to Achish to seek his servants: and Shimei went, and brought his servants from Gath.',
    'FIRST SAMUEL 12:3': 'Behold, here I am: witness against me before the LORD, and before his anointed: whose ox have I taken?  or whose ass have I taken?  or whom have I defrauded?  whom have I oppressed?  or of whose hand have I received any bribe to blind mine eyes therewith?  and I will restore it you.',
    'FIRST SAMUEL 15:3': 'Now go and smite Amalek, and utterly destroy all that they have, and spare them not; but slay both man and woman, infant and suckling, ox and sheep, camel and ass.',
    'FIRST SAMUEL 16:20': 'And Jesse took an ass laden with bread, and a bottle of wine, and a kid, and sent them by David his son unto Saul.',
    'FIRST SAMUEL 25:20': 'And it was so, as she rode on the ass, that she came down by the covert of the hill, and, behold, David and his men came down against her; and she met them.',
    'FIRST SAMUEL 25:23': 'And when Abigail saw David, she hasted, and lighted off the ass, and fell before David on her face, and bowed herself to the ground,',
    'FIRST SAMUEL 25:42': 'And Abigail hasted, and arose, and rode upon an ass, with five damsels of hers that went after her; and she went after the messengers of David, and became his wife.',
    'GENESIS 22:3': 'And Abraham rose up early in the morning, and saddled his ass, and took two of his young men with him, and Isaac his son, and clave the wood for the burnt offering, and rose up, and went unto the place of which God had told him.',
    'GENESIS 22:5': 'And Abraham said unto his young men, Abide ye here with the ass; and I and the lad will go yonder and worship, and come again to you,',
    'GENESIS 42:27': "And as one of them opened his sack to give his ass provender in the inn, he espied his money; for, behold, it was in his sack's mouth.",
    'GENESIS 44:13': 'Then they rent their clothes, and laded every man his ass, and returned to the city.',
    'GENESIS 49:11': "Binding his foal unto the vine, and his ass's colt unto the choice vine; he washed his garments in wine, and his clothes in the blood of grapes:",
    'GENESIS 49:14': 'Issachar is a strong ass couching down between two burdens:',
    'HOSEA 8:9': 'For they are gone up to Assyria, a wild ass alone by himself: Ephraim hath hired lovers.',
    'ISAIAH 1:3': "The ox knoweth his owner, and the ass his master's crib: but Israel doth not know, my people doth not consider.",
    'ISAIAH 32:20': 'Blessed are ye that sow beside all waters, that send forth thither the feet of the ox and the ass.',
    'JEREMIAH  22:19': 'He shall be buried with the burial of an ass, drawn and cast forth beyond the gates of Jerusalem.',
    'JEREMIAH  2:24': 'A wild ass used to the wilderness, that snuffeth up the wind at her pleasure; in her occasion who can turn her away?  all they that seek her will not weary themselves; in her month they shall find her.',
    'JOB 11:12': "For vain man would be wise, though man be born like a wild ass's colt.",
    'JOB 24:3': "They drive away the ass of the fatherless, they take the widow's ox for a pledge.",
    'JOB 39:5': 'Who hath sent out the wild ass free?  or who hath loosed the bands of the wild ass?',
    'JOB 6:5': 'Doth the wild ass bray when he hath grass?  or loweth the ox over his fodder? ',
    'JOHN 12:14': 'And Jesus, when he had found a young ass, sat thereon; as it is written,',
    'JOHN 12:15': "Fear not, daughter of Sion: behold, thy King cometh, sitting on an ass's colt.",
    'JOSHUA 15:18': 'And it came to pass, as she came unto him, that she moved him to ask of her father a field: and she lighted off her ass; and Caleb said unto her, What wouldest thou?',
    'JOSHUA 6:21': 'And they utterly destroyed all that was in the city, both man and woman, young and old, and ox, and sheep, and ass, with the edge of the sword.',
    'JUDGES 10:4': 'And he had thirty sons that rode on thirty ass colts, and they had thirty cities, which are called Havoth-jair unto this day, which are in the land of Gilead.',
    'JUDGES 12:14': 'And he had forty sons and thirty nephews, that rode on threescore and ten ass colts: and he judged Israel eight years.',
    'JUDGES 15:15': 'And he found a new jawbone of an ass, and put forth his hand, and took it, and slew a thousand men therewith.',
    'JUDGES 15:16': 'And Samson said, With the jawbone of an ass, heaps upon heaps, with the jaw of an ass have I slain a thousand men. ',
    'JUDGES 19:28': 'And he said unto her, Up, and let us be going.  But none answered.  Then the man took her up upon an ass, and the man rose up, and gat him unto his place. ',
    'JUDGES 1:14': 'And it came to pass, when she came to him, that she moved him to ask of her father a field: and she lighted from off her ass; and Caleb said unto her, What wilt thou?',
    'JUDGES 6:4': 'And they encamped against them, and destroyed the increase of the earth, till thou come unto Gaza, and left no sustenance for Israel, neither sheep, nor ox, nor ass.',
    'LUKE 13:15': 'The Lord then answered him, and said, Thou hypocrite, doth not each one of you on the sabbath loose his ox or his ass from the stall, and lead him away to watering?',
    'LUKE 14:5': 'And answered them, saying, Which of you shall have an ass or an ox fallen into a pit, and will not straightway pull him out on the sabbath day?',
    'MATTHEW 21:2': 'Saying unto them, Go into the village over against you, and straightway ye shall find an ass tied, and a colt with her: loose them, and bring them unto me.',
    'MATTHEW 21:5': 'Tell ye the daughter of Sion, Behold, thy King cometh unto thee, meek, and sitting upon an ass, and a colt the foal of an ass.',
    'MATTHEW 21:7': 'And brought the ass, and the colt, and put on them their clothes, and they set him thereon.',
    'NUMBERS 16:15': 'And Moses was very wroth, and said unto the LORD, Respect not thou their offering: I have not taken one ass from them, neither have I hurt one of them.',
    'NUMBERS 22:21': 'And Balaam rose up in the morning, and saddled his ass, and went with the princes of Moab.',
    'NUMBERS 22:22': "And God's anger was kindled because he went: and the angel of the LORD stood in the way for an adversary against him.  Now he was riding upon his ass, and his two servants were with him.",
    'NUMBERS 22:23': 'And the ass saw the angel of the LORD standing in the way, and his sword drawn in his hand: and the ass turned aside out of the way, and went into the field: and Balaam smote the ass, to turn her into the way.',
    'NUMBERS 22:25': "And when the ass saw the angel of the LORD, she thrust herself unto the wall, and crushed Balaam's foot against the wall: and he smote her again.",
    'NUMBERS 22:27': "And when the ass saw the angel of the LORD, she fell down under Balaam: and Balaam's anger was kindled, and he smote the ass with a staff.",
    'NUMBERS 22:28': 'And the LORD opened the mouth of the ass, and she said unto Balaam, What have I done unto thee, that thou hast smitten me these three times?',
    'NUMBERS 22:29': 'And Balaam said unto the ass, Because thou hast mocked me: I would there were a sword in mine hand, for now would I kill thee.',
    'NUMBERS 22:30': 'And the ass said unto Balaam, Am not I thine ass, upon which thou hast ridden ever since I was thine unto this day?  was I ever wont to do so unto thee?  And he said, Nay.',
    'NUMBERS 22:32': 'And the angel of the LORD said unto him, Wherefore hast thou smitten thine ass these three times?  behold, I went out to withstand thee, because thy way is perverse before me:',
    'NUMBERS 22:33': 'And the ass saw me, and turned from me these three times: unless she had turned from me, surely now also I had slain thee, and saved her alive.',
    'PROVERBS 26:3': "A whip for the horse, a bridle for the ass, and a rod for the fool's back.",
    'SECOND KINGS 4:24': 'Then she saddled an ass, and said to her servant, Drive, and go forward; slack not thy riding for me, except I bid thee.',
    'SECOND KINGS 6:25': "And there was a great famine in Samaria: and, behold, they besieged it, until an ass's head was sold for fourscore pieces of silver, and the fourth part of a cab of dove's dung for five pieces of silver.",
    'SECOND PETER 2:16': "But was rebuked for his iniquity: the dumb ass speaking with man's voice forbad the madness of the prophet",
    'SECOND SAMUEL 17:23': 'And when Ahithophel saw that his counsel was not followed, he saddled his ass, and arose, and gat him home to his house, to his city, and put his household in order, and hanged himself, and died, and was buried in the sepulchre of his father.',
    'SECOND SAMUEL 19:26': 'And he answered, My lord, O king, my servant deceived me: for thy servant said, I will saddle me an ass, that I may ride thereon, and go to the king; because thy servant is lame.',
    'ZECHARIAH 14:15': 'And so shall be the plague of the horse, of the mule, of the camel, and of the ass, and of all the beasts that shall be in these tents, as this plague.',
    'ZECHARIAH 9:9': 'Rejoice greatly, O daughter of Zion; shout, O daughter of Jerusalem: behold, thy King cometh unto thee: he is just, and having salvation; lowly, and riding upon an ass, and upon a colt the foal of an ass.'
}


class AsswordOfGod(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('passage.html')
        book = random.choice(ass_list.keys())
        passage = ass_list[book]
        template_values = {
            'book': book,
            'passage': passage,
        }
        self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', AsswordOfGod)],
                              debug=True)
