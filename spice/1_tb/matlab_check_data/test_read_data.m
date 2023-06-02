fileID = fopen('first_value_ro.txt', 'r');

data = fscanf(fileID, '%f');

fclose(fileID);
