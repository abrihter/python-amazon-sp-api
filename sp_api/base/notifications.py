from enum import Enum


class NotificationType(Enum):
    ANY_OFFER_CHANGED = 'ANY_OFFER_CHANGED'
    FEED_PROCESSING_FINISHED = 'FEED_PROCESSING_FINISHED'
    FBA_OUTBOUND_SHIPMENT_STATUS = 'FBA_OUTBOUND_SHIPMENT_STATUS'
    FEE_PROMOTION = 'FEE_PROMOTION'
    FULFILLMENT_ORDER_STATUS = 'FULFILLMENT_ORDER_STATUS'
    REPORT_PROCESSING_FINISHED = 'REPORT_PROCESSING_FINISHED'
    BRANDED_ITEM_CONTENT_CHANGE = 'BRANDED_ITEM_CONTENT_CHANGE'
    ITEM_PRODUCT_TYPE_CHANGE = 'ITEM_PRODUCT_TYPE_CHANGE'
    MFN_ORDER_STATUS_CHANGE = 'MFN_ORDER_STATUS_CHANGE'
    B2B_ANY_OFFER_CHANGED = 'B2B_ANY_OFFER_CHANGED'
