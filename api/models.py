##############################
### KENA MOBILE API MODELS ###
###      By @Matt0550      ###
##############################

from pydantic import BaseModel

from typing import Any, Dict, Optional

# ----------------------------
# Customer informations
# ----------------------------
class CustomerDTO(BaseModel):
    birthCountry: Optional[str] = None
    birthDate: Optional[str] = None
    birthLocation: Optional[str] = None
    birthProvince: Optional[str] = None
    citizenship: Optional[str] = None
    companyCity: Optional[Any] = None
    companyFax: Optional[Any] = None
    companyPhoneNumber: Optional[Any] = None
    customerId: Optional[int] = None
    documentTypeId: Optional[str] = None
    email: Optional[str] = None
    employee: Optional[str] = None
    gender: Optional[str] = None
    invoice: Optional[str] = None
    lastmod: Optional[str] = None
    lastname: Optional[str] = None
    mobileNumber: Optional[Any] = None
    name: Optional[str] = None
    novercaIccid: Optional[str] = None
    oldAccountType: Optional[Any] = None
    oldIccid: Optional[str] = None
    oldMsisdn: Optional[str] = None
    optionalConsent1: Optional[bool] = None
    optionalConsent2: Optional[bool] = None
    paymentType: Optional[str] = None
    personalDocumentCode: Optional[str] = None
    phoneNumber: Optional[str] = None
    psotalCode: Optional[Any] = None
    residenceAddress: Optional[str] = None
    residenceCity: Optional[str] = None
    residenceProvince: Optional[str] = None
    residenceStreetNumber: Optional[str] = None
    shippingAddress: Optional[Any] = None
    shippingAddressFirstName: Optional[Any] = None
    shippingAddressNumber: Optional[Any] = None
    shippingAddressProvince: Optional[Any] = None
    shippingAddressTown: Optional[Any] = None
    shippingAddressZipCode: Optional[Any] = None
    shippingLastname: Optional[Any] = None
    storeId: Optional[str] = None
    subscriptionStatus: Optional[Any] = None
    taxcode: Optional[str] = None
    vat: Optional[Any] = None
    warehouseId: Optional[Any] = None
    zipCode: Optional[Any] = None


# ----------------------------
# User credit informations
# ----------------------------
class UserCreditInfo(BaseModel):
    credit: Optional[str] = None
    dateActivation: Optional[str] = None
    falltime: Optional[str] = None
    pin1: Optional[str] = None
    puk1: Optional[str] = None
    pin2: Optional[str] = None
    puk2: Optional[str] = None
    tariffPlan: Optional[str] = None


# ----------------------------
# User promo informations
# ----------------------------
class AuxBagItem(BaseModel):
    name: Optional[str]
    value: Optional[int]
    unit: Optional[str]
    bundle_type: Optional[str]
    base_value: Optional[int]
    bagInitValue: Optional[int]

class TranslatedFields(BaseModel):
    title: Optional[str]
    description: Optional[str]
    short_description: Optional[str]
    description_tooltip: Optional[str]
    price: Optional[str]

class PromoModel(BaseModel):
    activable_by_user: Optional[int]
    startDate: Optional[str]
    endDate: Optional[str]
    promoName: Optional[str]
    name: Optional[str]
    subscriptionStatus: Optional[int]
    translated_fields: Optional[TranslatedFields]
    hasPendingCO: Optional[bool]
    said: Optional[int]
    auxBag: Optional[AuxBagItem]