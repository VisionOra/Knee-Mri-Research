<h1 style="text-align:center">Knee Mri Research</h1>

This research is to find out the condition of Knee-ligament. 

0. Healthy
1. Partial Ruptured
2. Fully Ruptured

![Knee Image](extras/knee_1.png)

<br>
<br>


<h1 style="text-align:center">DataSet Description</h1>

Main purpose of this data is to explore data-set, 

1. pkl files (Pickle) 
2. meta.csv

<br>

<h2 style="text-align:center">Description</h2>

KneeMRI dataset was gathered retrospectively from exam records made on a Siemens Avanto 1.5T MR scanner, and obtained by proton density-weighted fat suppression technique at the Clinical Hospital Centre Rijeka, Croatia, from 2006 until 2014. The dataset consists of 917 12-bit grayscale volumes of either left or right knees. Each volume record was assigned a diagnosis concerning the condition of the anterior cruciate ligament in a double-blind fashion, i.e. each volume record was labelled according to the ligament condition: (1) healthy, (2) partially injured, or (3) completely ruptured. A wider rectangular region of interest (ROI) was manually extracted from the original volumes and is also annotated. For more details regarding the dataset, the reader is referred to the paper stated under the "acknowledging source" section of this webpage.

This dataset was built with the intention of providing scientists, involved with machine vision and/or machine learning, an easy way of working with the data.

<br>

<h2 style="text-align:center">Anterior Cruciate Ligament (ACL) tears</h2>

In this project, we will specifically focus on Anterior Cruciate Ligament (ACL) tears which are the most common knee injuries among top athletes in soccer or basketball.
ACL tears happen when the anterior cruciate ligament is either stretched, partially torn, or completely torn. The most common injury is a complete tear.
Symptoms include pain, a popping sound during injury, instability of the knee, and joint swelling.
There are around 200,000 ACL tears each year in the United States, with over 100,000 ACL reconstruction surgeries per year.

<br>

<h2 style="text-align:center">Magnetic Resonance Imaging</h2>


Magnetic Resonance Imaging (MRI) is a medical imaging technique used in radiology to form a picture of the anatomy and the physiological processes of the body.
MRI is used to diagnose how well you responded to treatment as well as detecting tears and structural problems such as heart attacks, brain injury, blood vessel damage, etc.

<br>

<h2 style="text-align:center">Some considerations about the data 🤔</h2>

1. The slices are significantly different from a plane to another: this is the first thing I noticed as a non-specialist
2. Within a given plane, the slices may substantially differ as well. In fact, and we’ll see it later, some slices can better highlight an ACL tear
3. In the next post, we’ll build an MRI tear classification per plane. We’ll see next that the combination of these three models outperforms individual models
4. An MRI scan taken according to a given plane can be considered as a volume of stacked slices. As we previously said that cases don’t necessarily share the same of slices, MRIs cannot then be put in batches. We’ll see how to handle this efficiently.

<br>

 
<h2 style="text-align:center">File Attributes</h2>


    READ.ME         - file contains some basic information regarding this archive
    example.py      - Python script used to demonstrate how to access the files
    metadata.csv    - comma-delimited (csv) data containing descriptions of distinct volumes (header attribute information included)
    volumetric_data - directory containing all knee MR volumes, archived using 7-zip lossless file compression
    |-example.pck   - an example Python .pck file (just to inspect whether one wants to be bothered downloading the archive)
    |-vol01.7z      - compressed independent archive (1/10), containing 92 cases
    |-vol02.7z      - compressed independent archive (2/10), containing 92 cases
    |...
    |-vol10.7z      - compressed independent archive (10/10), containing the remaining 89 cases

<br>

<h2 style="text-align:center">Columns Description</h2>


1. **aclDiagnosis:**  The Lachman test is the most accurate test for detecting an ACL tear. Magnetic resonance imaging is the primary study used to diagnose ACL injury in the United States. It can also identify concomitant meniscal injury, collateral ligament tear, and bone contusions
    * Healthy
    * Half-Ruptured
    * Fully-Ruptured
    

2. **KneeLR:** Means if its left or right

<br>

<h2 style="text-align:center">ACKNOWLEDGING SOURCES:</h2>


If you are using this dataset in your work, please acknowledge the source (Clinical Hospital Centre Rijeka, Croatia) and reference this paper (preprint pdf):

I. Štajduhar, M. Mamula, D. Miletić, G. Unal, Semi-automated detection of anterior cruciate ligament injury from MRI, Computer Methods and Programs in Biomedicine, Volume 140, 2017, Pages 151–164.




![Knee Image](extras/knee_2.jpeg)


<br>

<h2 style="text-align:center">Plotting</h2>

We have pickle files in our dataset i.e volumetric data of scan, each pickle file consists of max 30 frames of mri-scan.

<br>

#### Healthy Knee

<br>

![scan1](extras/Healthy.gif)


<br>

#### Half Ruptured Knee

<br>

![scan1](extras/half_ruptured.gif)


<br>

#### Full Ruptured Knee

<br>

![scan1](extras/fully_ruptured.gif)


<br>
<br>

<h2 style="text-align:center">MRCNN Training</h2>

In MRCNN Training you will find trainig of MRI-Scans on MRCNN


Notbook to train MRCNN = [Link to Notebook](mrcnn_training/Train.ipynb)


