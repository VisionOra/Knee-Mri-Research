from shapely.geometry import box, Polygon
import numpy as np
from PIL import Image, ImageDraw
import cv2

def polygonIOU(label, pred):   # From the question.
    
    try:
        
        # Calculate Intersection and union, and tne IOU
        polygon1_shape,polygon2_shape =  Polygon(label), Polygon(pred)
        polygon_intersection = polygon1_shape.intersection(polygon2_shape).area
        polygon_union = polygon1_shape.union(polygon2_shape).area
        IOU = polygon_intersection / polygon_union 
    except ZeroDivisionError:
        IOU = 0
    
    return IOU

def rect_to_poly(points):
    
    x, y, w, h = points
    pts = np.asarray([
    [x     , y ],
    [x     , (y+h) ],
    [(x+w) , (y+h) ],
    [(x+w) , y ],

    ])
    
    return pts

def get_iou(bb1, bb2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters
    ----------
    bb1 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner
    bb2 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x, y) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner

    Returns
    -------
    float
        in [0, 1]
    """
    
    try:
        assert bb1['x1'] < bb1['x2']
        assert bb1['y1'] < bb1['y2']
        assert bb2['x1'] < bb2['x2']
        assert bb2['y1'] < bb2['y2']
    except:
        return 0

    # determine the coordinates of the intersection rectangle
    x_left = max(bb1['x1'], bb2['x1'])
    y_top = max(bb1['y1'], bb2['y1'])
    x_right = min(bb1['x2'], bb2['x2'])
    y_bottom = min(bb1['y2'], bb2['y2'])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    # compute the area of both AABBs
    bb1_area = (bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1'])
    bb2_area = (bb2['x2'] - bb2['x1']) * (bb2['y2'] - bb2['y1'])

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
    assert iou >= 0.0
    assert iou <= 1.0
    return iou


# def dice(pred, true, k = 1):
#     intersection = np.sum(pred[true==k]) * 2.0
#     dice = intersection / (np.sum(pred) + np.sum(true))
#     return dice

def dice(img, img2):
    if img.shape != img2.shape:
        raise ValueError("Shape mismatch: img and img2 must have to be of the same shape.")
    else:
        intersection = np.logical_and(img, img2)
        value = (2. * intersection.sum())  / (img.sum() + img2.sum())
    return value 


def jaccard(im1, im2):
    """
    Computes the Jaccard metric, a measure of set similarity.
    Parameters
    ----------
    im1 : array-like, bool
        Any array of arbitrary size. If not boolean, will be converted.
    im2 : array-like, bool
        Any other array of identical size. If not boolean, will be converted.
    Returns
    -------
    jaccard : float
        Jaccard metric returned is a float on range [0,1].
        Maximum similarity = 1
        No similarity = 0
    
    Notes
    -----
    The order of inputs for `jaccard` is irrelevant. The result will be
    identical if `im1` and `im2` are switched.
    """
    im1 = np.asarray(im1).astype(np.bool)
    im2 = np.asarray(im2).astype(np.bool)

    if im1.shape != im2.shape:
        raise ValueError("Shape mismatch: im1 and im2 must have the same shape.")

    intersection = np.logical_and(im1, im2)

    union = np.logical_or(im1, im2)

    return intersection.sum() / float(union.sum())


def make_mask(rect, image_shape):
    '''
    
        This fucntion is used to make mask of size of image and than plot while rectangle on it
        
        Params: rect        : (list)  : cordinates of rectangles   : [x1, x2, w, h]
        Params: image_shape : (tuple) : Shape of the image         : (224, 224)     
        
        Return: mask.       : (numpy.array) Masks w.r.t the image  :     
    '''
    w, h, _ = image_shape
    shape = rect

    # creating new Image object
    img = Image.new("RGB", (w, h))

    # create  rectangleimage
    img1 = ImageDraw.Draw(img)  
    img1.rectangle(shape, fill ="#FFFFFF")
    
    return np.asarray(img)



def mask_to_rect(image):
    '''
    
        Give rectangle cordinates according to the mask image
        
        
        Params: image : (numpy.array) Gray Scale Image
        
        Returns: Cordinates : (list) List of cordinates [x, y, w h]
    
    '''
    
    # Getting the Thresholds and ret
    ret,thresh = cv2.threshold(image, 0, 1, 0)
    
    # Checking the version of open cv I tried for (version 4)
    #    Getting contours on the bases of thresh
    if (int(cv2.__version__[0]) > 3):
        contours, hierarchy = cv2.findContours(thresh.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    else:
        im2, contours, hierarchy = cv2.findContours(thresh.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # Getting the biggest contour
    if len(contours) != 0:

        # find the biggest countour (c) by the area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        
    return [x, y, w, h]