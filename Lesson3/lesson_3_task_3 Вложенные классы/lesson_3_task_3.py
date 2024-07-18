from address import Address
from mailing import Mailing
letter = Mailing(Address("22", "Jump St", "14", "Hungtington Valley", "PA", "19006"), 
                 Address("5", "Heena Drive St", "45", "Los Angeles", "LA", "12305"), "$3", "2828282829")
print(f"Letter {letter.track} from: {letter.from_address} to: {letter.to_address}. Cost: {letter.cost}")