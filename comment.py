import cv2
import pytesseract
import os
import json

infographics = ['2014-12-11_01-28-02_UTC.jpg',
                '2015-03-14_20-16-42_UTC.jpg',
                '2015-03-20_17-36-05_UTC.jpg',
                '2015-03-21_02-59-01_UTC.jpg',
                '2015-04-12_05-37-29_UTC.jpg',
                '2015-04-12_05-44-05_UTC.jpg',
                '2015-04-26_16-50-35_UTC.jpg',
                '2015-04-28_18-50-10_UTC.jpg',
                '2015-04-30_15-59-41_UTC.jpg',
                '2015-05-01_02-13-39_UTC.jpg',
                '2015-08-10_01-16-10_UTC.jpg',
                '2015-08-23_17-57-50_UTC.jpg',
                '2015-08-24_23-47-07_UTC.jpg',
                '2015-08-26_03-24-16_UTC.jpg',
                '2016-02-03_20-17-08_UTC.jpg',
                '2016-02-03_20-42-31_UTC.jpg',
                '2016-02-05_19-38-39_UTC.jpg',
                '2016-02-09_22-49-47_UTC.jpg',
                '2016-02-10_19-26-08_UTC.jpg',
                '2016-02-16_19-16-42_UTC.jpg',
                '2016-02-18_21-51-28_UTC.jpg',
                '2016-02-20_19-15-44_UTC.jpg',
                '2016-02-23_21-59-40_UTC.jpg',
                '2016-02-26_23-39-08_UTC.jpg',
                '2016-02-29_23-36-55_UTC.jpg',
                '2016-02-29_23-39-14_UTC.jpg',
                '2016-04-21_21-14-55_UTC.jpg',
                '2016-05-03_21-35-51_UTC.jpg',
                '2016-09-23_14-16-24_UTC.jpg',
                '2016-09-23_15-35-59_UTC.jpg',
                '2016-09-24_22-19-02_UTC.jpg',
                '2016-09-28_15-41-36_UTC.jpg',
                '2016-09-28_19-30-13_UTC.jpg',
                '2016-09-29_02-09-00_UTC.jpg',
                '2016-09-30_13-27-59_UTC.jpg',
                '2016-10-09_02-55-12_UTC.jpg',
                '2016-10-29_02-44-52_UTC.jpg',
                '2016-11-18_18-44-31_UTC.jpg',
                '2016-11-24_20-49-03_UTC.jpg',
                '2016-11-27_01-13-30_UTC.jpg',
                '2016-12-19_20-05-47_UTC.jpg',
                '2017-02-01_14-10-18_UTC.jpg',
                '2017-02-03_21-04-17_UTC.jpg',
                '2017-02-07_01-15-07_UTC.jpg',
                '2017-02-08_23-33-10_UTC.jpg',
                '2017-02-10_17-39-14_UTC.jpg',
                '2017-02-11_22-11-29_UTC.jpg',
                '2017-02-14_17-52-29_UTC.jpg',
                '2017-02-17_01-21-05_UTC.jpg',
                '2017-02-17_20-29-34_UTC.jpg',
                '2017-02-22_03-04-33_UTC.jpg',
                '2017-02-22_03-08-57_UTC.jpg',
                '2017-02-23_02-26-04_UTC.jpg',
                '2017-02-25_03-31-43_UTC.jpg',
                '2017-02-26_22-59-17_UTC.jpg',
                '2017-02-27_01-43-46_UTC.jpg',
                '2017-02-28_17-22-05_UTC.jpg',
                '2017-03-10_19-32-48_UTC.jpg',
                '2017-03-25_16-55-17_UTC.jpg',
                '2017-04-27_14-51-18_UTC.jpg',
                '2017-05-14_16-44-54_UTC.jpg',
                '2017-05-14_16-46-23_UTC.jpg',
                '2017-05-22_17-08-30_UTC.jpg',
                '2017-05-23_16-39-29_UTC.jpg',
                '2017-06-07_17-31-27_UTC.jpg',
                '2017-06-26_21-48-42_UTC_1.jpg',
                '2017-07-05_19-01-25_UTC.jpg',
                '2017-07-13_07-15-46_UTC.jpg',
                '2017-07-14_17-11-18_UTC.jpg',
                '2017-07-15_20-01-33_UTC.jpg',
                '2017-08-07_22-10-58_UTC_1.jpg',
                '2017-08-07_22-10-58_UTC_2.jpg',
                '2017-08-09_13-34-58_UTC.jpg',
                '2017-08-09_20-45-24_UTC.jpg',
                '2017-08-21_06-26-40_UTC.jpg',
                '2017-10-16_15-47-17_UTC.jpg',
                '2017-11-22_23-29-22_UTC.jpg',
                '2017-12-08_02-39-29_UTC.jpg',
                '2017-12-08_17-35-04_UTC.jpg',
                '2017-12-10_23-12-46_UTC.jpg',
                '2017-12-13_17-09-03_UTC.jpg',
                '2017-12-13_18-39-45_UTC.jpg',
                '2018-02-01_18-06-35_UTC.jpg',
                '2018-02-02_15-17-49_UTC.jpg',
                '2018-02-05_20-11-19_UTC.jpg',
                '2018-02-28_17-35-36_UTC.jpg',
                '2018-03-05_18-37-08_UTC.jpg',
                '2018-03-25_17-13-20_UTC.jpg',
                '2018-03-27_14-43-11_UTC_2.jpg',
                '2018-03-27_18-12-20_UTC.jpg',
                '2018-04-03_15-05-05_UTC.jpg',
                '2018-04-04_18-29-26_UTC_1.jpg',
                '2018-04-04_18-29-26_UTC_2.jpg',
                '2018-04-04_18-29-26_UTC_3.jpg',
                '2018-04-04_18-29-26_UTC_4.jpg',
                '2018-04-10_17-39-48_UTC_1.jpg',
                '2018-04-11_17-34-29_UTC.jpg',
                '2018-05-16_18-17-06_UTC.jpg',
                '2018-06-19_19-43-31_UTC.jpg',
                '2018-06-23_16-22-17_UTC_1.jpg',
                '2018-06-23_16-22-17_UTC_2.jpg',
                '2018-07-05_02-23-34_UTC.jpg',
                '2018-07-05_05-52-03_UTC.jpg',
                '2018-07-05_06-32-11_UTC.jpg',
                '2018-07-13_19-15-54_UTC.jpg',
                '2018-07-14_16-43-45_UTC.jpg',
                '2018-08-09_21-56-56_UTC.jpg',
                '2018-08-11_19-24-14_UTC.jpg',
                '2018-08-12_17-03-21_UTC.jpg',
                '2018-08-22_20-28-40_UTC.jpg',
                '2018-09-27_04-22-34_UTC.jpg',
                '2018-10-12_13-44-59_UTC.jpg',
                '2018-10-12_19-01-18_UTC.jpg',
                '2018-11-01_21-00-00_UTC.jpg',
                '2018-11-02_14-00-55_UTC.jpg',
                '2018-11-03_12-41-03_UTC.jpg',
                '2018-11-05_06-30-45_UTC.jpg',
                '2018-11-05_18-32-58_UTC.jpg',
                '2018-11-05_22-16-54_UTC.jpg',
                '2018-11-07_14-49-21_UTC.jpg',
                '2018-11-07_14-51-06_UTC.jpg',
                '2018-11-07_14-53-09_UTC.jpg',
                '2018-11-07_14-56-55_UTC.jpg',
                '2018-11-07_15-17-28_UTC.jpg',
                '2018-11-07_15-19-00_UTC.jpg',
                '2018-11-07_15-19-46_UTC.jpg',
                '2018-11-07_15-24-48_UTC.jpg',
                '2018-11-07_22-27-04_UTC.jpg',
                '2018-11-13_15-40-12_UTC_1.jpg',
                '2018-11-13_15-40-12_UTC_2.jpg',
                '2018-11-13_23-55-52_UTC.jpg',
                '2018-11-14_15-22-02_UTC_2.jpg',
                '2018-11-17_20-31-09_UTC_1.jpg',
                '2018-11-23_17-04-19_UTC.jpg',
                '2018-11-27_23-49-04_UTC.jpg',
                '2018-12-07_01-01-24_UTC_1.jpg',
                '2018-12-11_00-46-51_UTC.jpg',
                '2018-12-15_02-32-33_UTC.jpg',
                '2018-12-16_00-22-09_UTC_2.jpg',
                '2018-12-18_18-44-04_UTC.jpg',
                '2018-12-21_00-38-58_UTC_1.jpg',
                '2018-12-21_00-38-58_UTC_2.jpg',
                '2018-12-22_20-14-39_UTC_1.jpg',
                '2018-12-22_20-14-39_UTC_5.jpg',
                '2019-01-01_04-56-12_UTC_1.jpg',
                '2019-01-01_04-56-12_UTC_2.jpg',
                '2019-01-01_04-56-12_UTC_3.jpg',
                '2019-01-01_04-56-12_UTC_4.jpg',
                '2019-01-21_15-41-53_UTC.jpg',
                '2019-02-02_02-43-58_UTC_1.jpg',
                '2019-02-02_02-43-58_UTC_2.jpg',
                '2019-02-04_14-34-05_UTC.jpg',
                '2019-02-04_20-30-23_UTC.jpg',
                '2019-02-11_19-09-33_UTC.jpg',
                '2019-02-15_17-32-21_UTC_1.jpg',
                '2019-02-15_17-32-21_UTC_2.jpg',
                '2019-02-15_17-32-21_UTC_3.jpg',
                '2019-02-21_00-26-21_UTC_1.jpg',
                '2019-02-23_22-02-33_UTC_1.jpg',
                '2019-02-24_19-48-52_UTC.jpg',
                '2019-03-06_23-56-06_UTC.jpg',
                '2019-03-09_00-36-26_UTC_1.jpg',
                '2019-03-09_00-36-26_UTC_3.jpg',
                '2019-03-12_22-32-24_UTC.jpg',
                '2019-03-13_21-35-39_UTC.jpg',
                '2019-03-15_16-42-48_UTC_1.jpg',
                '2019-03-18_21-17-55_UTC.jpg',
                '2019-03-20_15-04-43_UTC.jpg',
                '2019-03-26_21-49-38_UTC_1.jpg',
                '2019-03-28_16-52-40_UTC_1.jpg',
                '2019-03-30_20-58-27_UTC.jpg',
                '2019-04-01_02-01-48_UTC.jpg',
                '2019-04-06_00-53-53_UTC.jpg',
                '2019-04-09_21-48-43_UTC_5.jpg',
                '2019-04-13_20-15-14_UTC.jpg',
                '2019-05-02_21-11-23_UTC_1.jpg',
                '2019-05-02_21-11-23_UTC_2.jpg',
                '2019-06-19_17-12-26_UTC.jpg',
                '2019-06-26_22-45-29_UTC.jpg',
                '2019-07-06_02-38-40_UTC.jpg',
                '2019-07-13_14-47-05_UTC.jpg',
                '2019-07-17_00-47-08_UTC.jpg',
                '2019-08-02_03-55-42_UTC.jpg',
                '2019-08-06_17-51-10_UTC.jpg',
                '2019-08-09_17-46-09_UTC.jpg',
                '2019-08-19_23-51-53_UTC_1.jpg',
                '2019-08-19_23-51-53_UTC_2.jpg',
                '2019-08-19_23-51-53_UTC_3.jpg',
                '2019-08-28_22-31-19_UTC.jpg',
                '2019-09-19_00-55-38_UTC_1.jpg',
                '2019-09-19_00-55-38_UTC_2.jpg',
                '2019-09-19_00-55-38_UTC_3.jpg',
                '2019-11-19_19-35-12_UTC.jpg',
                '2019-11-23_14-47-08_UTC.jpg',
                '2020-01-01_16-04-26_UTC.jpg',
                '2020-01-20_16-22-39_UTC.jpg',
                '2020-01-26_23-50-49_UTC.jpg',
                '2020-02-01_22-19-57_UTC.jpg',
                '2020-02-04_16-43-56_UTC.jpg',
                '2020-02-05_21-39-36_UTC.jpg',
                '2020-03-07_20-34-09_UTC.jpg',
                '2020-03-08_17-18-58_UTC.jpg',
                '2020-03-29_16-12-16_UTC.jpg',
                '2020-04-01_15-58-35_UTC.jpg',
                '2020-04-01_18-47-31_UTC.jpg',
                '2020-04-09_22-01-20_UTC.jpg',
                '2020-05-06_20-48-26_UTC.jpg',
                '2020-05-12_19-39-49_UTC.jpg',
                '2020-05-13_00-39-26_UTC.jpg',
                '2020-05-13_00-43-24_UTC.jpg',
                '2020-05-13_22-05-44_UTC_1.jpg',
                '2020-05-13_22-05-44_UTC_2.jpg',
                '2020-05-20_00-20-37_UTC.jpg',
                '2020-05-22_22-18-59_UTC.jpg',
                '2020-05-25_23-01-28_UTC.jpg',
                '2020-05-31_00-55-25_UTC.jpg',
                '2020-06-04_22-22-46_UTC.jpg',
                '2020-06-14_18-59-34_UTC.jpg',
                '2020-06-27_16-12-02_UTC.jpg',
                '2020-06-28_15-00-16_UTC.jpg',
                '2020-06-29_15-39-31_UTC.jpg',
                '2020-07-03_19-08-18_UTC.jpg',
                '2020-07-18_17-30-54_UTC.jpg',
                '2020-07-20_15-09-29_UTC.jpg',
                '2020-07-24_00-10-54_UTC.jpg',
                '2020-07-29_19-15-50_UTC_1.jpg',
                '2020-07-29_19-15-50_UTC_2.jpg',
                '2020-07-29_19-15-50_UTC_3.jpg',
                '2020-07-29_19-15-50_UTC_4.jpg',
                '2020-08-01_18-34-37_UTC.jpg',
                '2020-08-02_17-35-23_UTC.jpg',
                '2020-08-04_21-50-22_UTC.jpg',
                '2020-08-04_23-42-08_UTC.jpg',
                '2020-08-05_18-00-59_UTC.jpg',
                '2020-08-06_17-11-26_UTC.jpg',
                '2020-08-07_18-06-34_UTC.jpg',
                '2020-08-08_18-22-55_UTC.jpg',
                '2020-08-09_16-30-14_UTC.jpg',
                '2020-08-11_18-25-49_UTC.jpg',
                '2020-08-15_17-46-54_UTC.jpg',
                '2020-08-16_18-37-48_UTC.jpg',
                '2020-08-17_14-54-30_UTC_1.jpg',
                '2020-08-17_14-54-30_UTC_10.jpg',
                '2020-08-17_14-54-30_UTC_2.jpg',
                '2020-08-17_14-54-30_UTC_3.jpg',
                '2020-08-17_14-54-30_UTC_4.jpg',
                '2020-08-17_14-54-30_UTC_5.jpg',
                '2020-08-17_14-54-30_UTC_6.jpg',
                '2020-08-17_14-54-30_UTC_7.jpg',
                '2020-08-17_14-54-30_UTC_8.jpg',
                '2020-08-17_14-54-30_UTC_9.jpg',
                '2020-08-19_01-01-33_UTC.jpg',
                '2020-08-19_18-23-00_UTC.jpg',
                '2020-08-21_15-42-51_UTC.jpg',
                '2020-08-24_16-26-37_UTC.jpg',
                '2020-08-27_00-14-23_UTC.jpg',
                '2020-08-27_19-32-15_UTC.jpg',
                '2020-08-28_14-22-21_UTC.jpg',
                '2020-08-29_05-14-17_UTC.jpg',
                '2020-08-29_22-46-17_UTC.jpg',
                '2020-08-30_17-27-47_UTC.jpg',
                '2020-09-01_17-02-36_UTC.jpg',
                '2020-09-04_04-01-47_UTC.jpg',
                '2020-09-05_00-16-19_UTC.jpg',
                '2020-09-08_19-51-32_UTC.jpg',
                '2020-09-12_02-59-28_UTC.jpg',
                '2020-09-12_03-13-45_UTC.jpg',
                '2020-09-13_02-08-48_UTC.jpg',
                '2020-09-16_18-23-45_UTC.jpg',
                '2020-09-18_17-37-01_UTC.jpg',
                '2020-09-19_01-37-34_UTC.jpg',
                '2020-09-22_18-24-44_UTC.jpg',
                '2020-09-23_19-29-39_UTC.jpg',
                '2020-09-23_21-42-08_UTC.jpg',
                '2020-09-25_20-19-58_UTC.jpg',
                '2020-09-28_18-21-45_UTC.jpg',
                '2020-09-29_14-26-01_UTC_1.jpg',
                '2020-09-29_14-26-01_UTC_2.jpg',
                '2020-09-29_14-26-01_UTC_3.jpg',
                '2020-09-29_14-26-01_UTC_4.jpg',
                '2020-09-29_14-26-01_UTC_5.jpg',
                '2020-09-29_14-26-01_UTC_6.jpg',
                '2020-09-29_22-46-45_UTC.jpg',
                '2020-10-01_03-29-17_UTC.jpg',
                '2020-10-01_14-00-32_UTC.jpg',
                '2020-10-02_20-12-08_UTC.jpg',
                '2020-10-05_01-40-17_UTC.jpg',
                '2020-10-05_19-28-11_UTC.jpg',
                '2020-10-07_00-01-40_UTC.jpg',
                '2020-10-07_18-36-52_UTC.jpg',
                '2020-10-09_15-01-40_UTC.jpg',
                '2020-10-09_15-54-31_UTC.jpg',
                '2020-10-11_02-04-38_UTC_1.jpg',
                '2020-10-11_23-53-16_UTC.jpg',
                '2020-10-12_14-36-25_UTC.jpg',
                '2020-10-13_14-16-49_UTC.jpg',
                '2020-10-14_15-38-27_UTC.jpg',
                '2020-10-14_18-14-26_UTC.jpg',
                '2020-10-15_22-26-17_UTC_1.jpg',
                '2020-10-15_22-26-17_UTC_2.jpg',
                '2020-10-15_22-26-17_UTC_3.jpg',
                '2020-10-16_17-44-36_UTC.jpg',
                '2020-10-18_18-49-21_UTC.jpg',
                '2020-10-20_23-18-12_UTC.jpg',
                '2020-10-22_18-28-04_UTC.jpg',
                '2020-10-22_20-04-07_UTC_1.jpg',
                '2020-10-22_20-04-07_UTC_2.jpg',
                '2020-10-22_20-04-07_UTC_3.jpg',
                '2020-10-22_20-04-07_UTC_4.jpg',
                '2020-10-27_22-32-58_UTC.jpg',
                '2020-10-30_21-31-17_UTC.jpg',
                '2020-10-31_20-09-04_UTC.jpg',
                '2020-11-02_01-53-14_UTC_1.jpg',
                '2020-11-03_19-25-43_UTC.jpg',
                '2020-11-04_14-56-25_UTC.jpg',
                '2020-11-04_22-34-54_UTC.jpg',
                '2020-11-06_23-53-51_UTC.jpg',
                '2020-11-07_16-53-19_UTC_1.jpg',
                '2020-11-07_16-53-19_UTC_2.jpg',
                '2020-11-07_19-06-37_UTC.jpg',
                '2020-11-12_18-59-25_UTC.jpg',
                '2020-11-16_17-29-53_UTC.jpg',
                '2020-11-18_23-09-48_UTC_1.jpg',
                '2020-11-18_23-09-48_UTC_2.jpg',
                '2020-11-18_23-09-48_UTC_3.jpg',
                '2020-11-20_15-19-24_UTC.jpg',
                '2020-11-20_22-00-56_UTC.jpg',
                '2020-11-24_17-56-57_UTC.jpg',
                '2020-11-26_00-33-31_UTC.jpg',
                '2020-11-28_21-45-10_UTC.jpg',
                '2020-12-02_02-12-39_UTC_1.jpg',
                '2020-12-02_02-12-39_UTC_2.jpg',
                '2020-12-02_02-12-39_UTC_3.jpg',
                '2020-12-02_20-59-15_UTC.jpg',
                '2020-12-03_16-32-55_UTC.jpg',
                '2020-12-07_23-35-26_UTC.jpg',
                '2020-12-09_22-20-26_UTC.jpg',
                '2020-12-11_22-44-17_UTC.jpg',
                '2020-12-13_01-01-21_UTC.jpg',
                '2020-12-14_20-10-30_UTC.jpg',
                '2020-12-15_23-47-42_UTC.jpg',
                '2020-12-26_21-06-03_UTC.jpg',
                '2020-12-27_20-24-16_UTC.jpg',
                '2020-12-28_18-03-20_UTC.jpg',
                '2020-12-29_19-48-18_UTC_1.jpg',
                '2020-12-29_19-48-18_UTC_2.jpg',
                '2020-12-30_18-41-56_UTC.jpg',
                '2020-12-31_15-53-25_UTC.jpg',
                '2020-12-31_19-32-36_UTC.jpg']


def count_words(string):
    # Removing the spaces from start and end
    string1 = string.strip()
    # Initializing the count from 1 because we there is no space at the last
    count = 1
    # Iterating through the string
    for i in string1:
        # If we encounter space, increment the count with 1.
        if i == " ":
            count += 1

    return count


def stats(path):
    # Total number of comments on nonaction infographic posts
    total_nonactioninf_comments = 0
    # Total number of comments on action infographic posts
    total_actioninf_comments = 0
    # Number of action comments on nonaction infographic posts
    action_nonactioninf_comments = 0
    # Number of action comments on action infographic posts
    action_actioninf_comments = 0

    # Total number of commented words on nonaction infographic posts
    total_nonactioninf_words = 0
    # Total number of commented words on action infographic posts
    total_actioninf_words = 0
    # Number of action words on nonaction infographic posts
    action_nonactioninf_words = 0
    # Number of action words on action infographic posts
    action_actioninf_words = 0
    # Number of posts (split by number of infographic action words in the post)
    num_posts = {0: 0, 1: 0, 2: 0, 3: 0,
                 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0}
    # Total number of posts
    total_num_posts = 0
    # Total number of comments (split by number of infographic action words in the post)
    total_comments_by_num = {0: 0, 1: 0, 2: 0, 3: 0,
                             4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0}
    # Number of action comments (split by number of infographic action words in the post)
    action_comments_by_num = {0: 0, 1: 0, 2: 0, 3: 0,
                              4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0}
    # Total number of words (split by number of infographic action words in the post)
    total_words_by_num = {0: 0, 1: 0, 2: 0, 3: 0,
                          4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0}
    # Number of commented action words (split by number of infographic action words in the post)
    action_words_by_num = {0: 0, 1: 0, 2: 0, 3: 0,
                           4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0}
    # Action Word Bank (including various tenses when this is not already included in the word)
    action_words = ["resist", "petition", "call", "vote", "voting", "march", "rise", "text", "act", "demand", "fight", "protest", "share", "sharing", "come", "coming",
                    "support", "help", "urge", "urging", "sign", "prosecute", "prosecuting", "donate", "donating", "defend", "change", "changing", "command", "shout", "cry",
                    "react", "now", "justice", "read", "stop", "manifest", "join", "give", "giving", "lift", "assert", "protect", "stand", "take", "taking", "say", "liberate",
                    "liberating", "return", "heal", "raise", "raising", "end", "register", "contact", "bring", "hear", "listen", "watch", "release", "releasing", "strike", "preach",
                    "abolish", "free", "defund", "duty", "email", "post", "abolition"]

    for filename in os.listdir(path):
        # Evaluate comments jsons
        if filename.endswith("comments.json"):
            comment_count = 0  # Comments for this post
            action_comment_count = 0  # Action comments for this post
            word_count = 0  # Comment words for this post
            action_word_count = 0  # Action comment words for this post
            print("========= FILE ", filename, " ==========")
            # Load JSON file
            new_json_path = os.path.join(path, filename)
            file = open(new_json_path)
            data = json.load(file)
            # Iterate through comments to extract number of action/total comments/words
            for comment in data:
                # This constant represents the first instant of 2021; we exclude comments after 2021
                if comment["created_at"] < 1609459200:
                    text = comment["text"]
                    text = text.lower()

                    # Words
                    comment_action_words = 0
                    for word in action_words:
                        comment_action_words += text.count(word)
                    action_word_count += comment_action_words
                    word_count += count_words(text)

                    # Comments
                    bool = False
                    for word in action_words:
                        if text.count(word) > 0:
                            bool = True
                    if bool:
                        action_comment_count += 1
                    comment_count += 1
            # Get the image
            images_path = path + "-images"
            filename = filename.replace("_comments.json", ".jpg")
            new_path = os.path.join(images_path, filename)
            filenames = []
            if os.path.isfile(new_path):
                filenames.append(filename)
            else:
                filename = filename.replace(".jpg", "")
                for i in range(1, 11):  # Iterate through slides
                    filenames.append(filename + "_" + str(i) + ".jpg")
            post_action_words = 0
            num_infographic_in_post = 0
            for filename in filenames:
                if not filename in infographics:
                    continue
                num_infographic_in_post += 1
                new_path = os.path.join(images_path, filename)
                img = cv2.imread(new_path)
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # Extract text from the image
                text = pytesseract.image_to_string(img_rgb)

                # Make text lowercase (for action word detection) and remove newlines (for readability)
                lowercase_text = text.lower()
                lowercase_text = lowercase_text.replace("\n", " ")
                lowercase_text_no_space_new = lowercase_text.replace("\n", "")
                # Add number of action words to action words
                for word in action_words:
                    post_action_words += lowercase_text_no_space_new.count(
                        word)
            if num_infographic_in_post > 0:  # Infographic post
                num_posts[post_action_words] += 1
                total_num_posts += 1
                # Add to aggregated statistic
                if post_action_words > 0:
                    total_actioninf_comments += comment_count
                    action_actioninf_comments += action_comment_count
                    total_actioninf_words += word_count
                    action_actioninf_words += action_word_count
                else:
                    total_nonactioninf_comments += comment_count
                    action_nonactioninf_comments += action_comment_count
                    total_nonactioninf_words += word_count
                    action_nonactioninf_words += action_word_count
                # Add to by-num statistic
                total_comments_by_num[post_action_words] += comment_count
                action_comments_by_num[post_action_words] += action_comment_count
                total_words_by_num[post_action_words] += word_count
                action_words_by_num[post_action_words] += action_word_count
    print("=============== BY NUM ==============")
    for i in range(0, 21):
        if total_comments_by_num[i] > 0 or total_words_by_num[i] > 0:
            print("===", i, "===")
            print("COMMENTS")
            print("action comments percent: ", 100 *
                  action_comments_by_num[i]/total_comments_by_num[i])
            print("action_comments_by_num", action_comments_by_num[i])
            print("total_comments_by_num", total_comments_by_num[i])

            print("WORDS")
            print("action words percent: ", 100 *
                  action_words_by_num[i]/total_words_by_num[i])
            print("action_words_by_num", action_words_by_num[i])
            print("total_words_by_num", total_words_by_num[i])

            print("NUM POSTS")
            print("num_posts", num_posts[i])

    print("=============== AGGREGATED ==============")
    print("COMMENTS")
    print("The percentage of comments on action infographics which were action comments: ",
          100 * action_actioninf_comments/total_actioninf_comments)
    print("The percentage of comments on nonaction infographics which were action comments: ", 100 * action_nonactioninf_comments /
          total_nonactioninf_comments)
    print("Number of action comments on action infographic posts: ",
          action_actioninf_comments)
    print("Total number of comments on action infographic posts: ",
          total_actioninf_comments)
    print("Number of action comments on nonaction infographic posts: ",
          action_nonactioninf_comments)
    print("Total number of comments on nonaction infographic posts: ",
          total_nonactioninf_comments)
    print("WORDS")
    print("The percentage of commented words on action infographics which were action words: ",
          100 * action_actioninf_words/total_actioninf_words)
    print("The percentage of commented words on nonaction infographics which were action words: ", 100 * action_nonactioninf_words /
          total_nonactioninf_words)
    print("Number of commented action words on action infographic posts: ",
          action_actioninf_words)
    print("Total number of commented words on action infographic posts: ",
          total_actioninf_words)
    print("Number of commented action words on nonaction infographic posts: ",
          action_nonactioninf_words)
    print("Total number of commented action words on nonaction infographic posts: ",
          total_nonactioninf_words)

    print("Total number of posts: ", total_num_posts)


stats(insert_path_here)
