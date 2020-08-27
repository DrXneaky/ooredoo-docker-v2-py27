
@ECHO OFF
cd nginx\ooredoo-front
rmdir /q /s dist
echo ====== Building production.. =====
call ng build --prod
echo ====== Build succeeded =======
cd ..
cd nginx
echo ======= removing old dist folder ==========
rmdir /q /s dist
mkdir dist
echo ====== Copying files.. =====
xcopy ooredoo-front\dist\network-automation-ooredoo\* dist\  /s /i /Y
echo ====== Copying is finished.. =====


cd..
cd

echo ========== git add ..==========
git add .

echo ========== committing changes ==========
git commit -am "some changes"

echo =======================================================
echo =========== pushing to github repository =========
git push -u origin master
echo ========== push succeeded =============
pause
