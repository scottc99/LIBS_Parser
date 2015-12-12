% Plotting and exporting the Spectra
% Change the file path to meet your needs.
%Assume sampling frequency of one FIR-stable IIR-call christine or bless
tic
XFiltered=zeros(500,12288);

for K= 1:500 %for each rock trial 1-500 (1:1 to quicken process while prototyping
N = 12288;
M=24;   % Number of XRF points
I = 1:1:N;
X(K,:) = rock_data_unfiltered.X(K,1:N); %unfilter Spec
Y1(K,:) =rock_data_unfiltered.Y(K,1:M); % XRF
XFiltered(K,:) = transpose(smooth(X(K,:),'sgolay',2)); %filterhere define XFiltered
rock_data=struct('X',X,'Xfiltered',XFiltered,'Y',Y1)
end

X(1,:) = rock_data_unfiltered.X(1,1:N);

for J= 40:12258
XFiltered(1,J) = (rock_data_unfiltered.X(1,J)+rock_data_unfiltered.X(1,J+1)+rock_data_unfiltered.X(1,J+2)+rock_data_unfiltered.X(1,J+3)+rock_data_unfiltered.X(1,J+4)+rock_data_unfiltered.X(1,J+5)+rock_data_unfiltered.X(1,J+6)+rock_data_unfiltered.X(1,J+7)+rock_data_unfiltered.X(1,J+8)+rock_data_unfiltered.X(1,J+9)+rock_data_unfiltered.X(1,J+10)+rock_data_unfiltered.X(1,J+11)+rock_data_unfiltered.X(1,J+12)+rock_data_unfiltered.X(1,J+13)+rock_data_unfiltered.X(1,J+14)+rock_data_unfiltered.X(1,J+15)+rock_data_unfiltered.X(1,J+16)+rock_data_unfiltered.X(1,J+18)+rock_data_unfiltered.X(1,J+19)+rock_data_unfiltered.X(1,J+20)+rock_data_unfiltered.X(1,J+21)+rock_data_unfiltered.X(1,J+22)+rock_data_unfiltered.X(1,J+23)+rock_data_unfiltered.X(1,J+24)+rock_data_unfiltered.X(1,J+25)+rock_data_unfiltered.X(1,J+26)+rock_data_unfiltered.X(1,J+27)+rock_data_unfiltered.X(1,J+28)+rock_data_unfiltered.X(1,J+29)+rock_data_unfiltered.X(1,J-1)+rock_data_unfiltered.X(1,J-2)+rock_data_unfiltered.X(1,J-3)+rock_data_unfiltered.X(1,J-4)+rock_data_unfiltered.X(1,J-5)+rock_data_unfiltered.X(1,J-6)+rock_data_unfiltered.X(1,J-7)+rock_data_unfiltered.X(1,J-8)+rock_data_unfiltered.X(1,J-9)+rock_data_unfiltered.X(1,J-10)+rock_data_unfiltered.X(1,J-11)+rock_data_unfiltered.X(1,J-12)+rock_data_unfiltered.X(1,J-13)+rock_data_unfiltered.X(1,J-14)+rock_data_unfiltered.X(1,J-15)+rock_data_unfiltered.X(1,J-16)+rock_data_unfiltered.X(1,J-17)+rock_data_unfiltered.X(1,J-18)+rock_data_unfiltered.X(1,J-19)+rock_data_unfiltered.X(1,J-20)+rock_data_unfiltered.X(1,J-21)+rock_data_unfiltered.X(1,J-22)+rock_data_unfiltered.X(1,J-23)+rock_data_unfiltered.X(1,J-24)+rock_data_unfiltered.X(1,J-25)+rock_data_unfiltered.X(1,J-26)+rock_data_unfiltered.X(1,J-27)+rock_data_unfiltered.X(1,J-28)+rock_data_unfiltered.X(1,J-29))/59;
end

XX(1,:)=smooth(X(1,:))-smooth(XFiltered(1,:));


figure
subplot(1,3,1), plot(smooth(X(1,:))); 
subplot(1,3,2), plot(smooth(XFiltered(1,:))); 
subplot(1,3,3), plot(XXX(1,:))
toc