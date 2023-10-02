A_SCORE = 70
B_SCORE = 60
C_SCORE = 50
D_SCORE = 40
E_SCORE = 30

# GET SCORE FROM THE USER
Eng_Score = int(input('What is Your English Score? '))
Mth_Score = int(input('What is your Mathematics Score? '))
Phy_Score = int(input('What is your Physics Score? '))
Chm_Score = int(input('What is your Chemistry Score? '))
Bio_Score = int(input('What is your Biology Score? '))
print()

# THE RESULT

# ENGLISH

if Eng_Score >= A_SCORE:
    print('Your English Grade is A.')
elif Eng_Score >= B_SCORE:
    print('Your English Grade is B.')
elif Eng_Score >= C_SCORE:
    print('Your English Grade is C.')
elif Eng_Score >= D_SCORE:
    print('Your English Grade is D.')
elif Eng_Score >= E_SCORE:
    print('Your English Grade is E.')
else:
    print('Your English Grade is F.')

# MATHEMATICS

if Mth_Score >= A_SCORE:
    print('Your Mathematics Grade is A.')
elif Mth_Score >= B_SCORE:
    print('Your Mathematics Grade is B.')
elif Mth_Score >= C_SCORE:
    print('Your Mathematics Grade is C.')
elif Mth_Score >= D_SCORE:
    print('Your Mathematics Grade is D.')
elif Mth_Score >= E_SCORE:
    print('Your Mathematics Grade is E.')
else:
    print('Your Mathematics Grade is F.')

# PHYSICS

if Phy_Score >= A_SCORE:
    print('Your Physics Grade is A.')
elif Phy_Score >= B_SCORE:
    print('Your Physics Grade is B.')
elif Phy_Score >= C_SCORE:
    print('Your Physics Grade is C.')
elif Phy_Score >= D_SCORE:
    print('Your Physics Grade is D.')
elif Phy_Score >= E_SCORE:
    print('Your Physics Grade is E.')
else:
    print('Your Physics Grade is F.')

# CHEMISTRY

if Chm_Score >= A_SCORE:
    print('Your Chemistry Grade is A.')
elif Chm_Score >= B_SCORE:
    print('Your Chemistry Grade is B.')
elif Chm_Score >= C_SCORE:
    print('Your Chemistry Grade is C.')
elif Chm_Score >= D_SCORE:
    print('Your Chemistry Grade is D.')
elif Chm_Score >= E_SCORE:
    print('Your Chemistry Grade is E.')
else:
    print('Your Chemistry Grade is F.')

# BILOGY

if Bio_Score >= A_SCORE:
    print('Your Biology Grade is A.')
elif Bio_Score >= B_SCORE:
    print('Your Biology Grade is B.')
elif Bio_Score >= C_SCORE:
    print('Your Biology Grade is C.')
elif Bio_Score >= D_SCORE:
    print('Your Biology Grade is D.')
elif Bio_Score >= E_SCORE:
    print('Your Biology Grade is E.')
else:
    print('Your Biology Grade is F.')