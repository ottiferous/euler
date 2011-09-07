#	=============
#	Timer Wrapper
#	=============
if [ "$1" == "-l" ]; then
	echo "==========	LOG        =========="
	for each in *.py
	do
		echo -n "$each"
		python -m profile $each
		echo "=========================================="
	done
	echo "==========	END        =========="
else
	echo "     =====     SHORT LOG     =====     "
	for each in *.py
	do
		script=$(echo "$each" | cut -d "." -f1)
		echo -en "*$script*\t--\t"
		line=`python -m profile $each | grep CPU`
		line=$(echo "$line" | cut -d " " -f 14)
		echo -e "*$line seconds*"
	done
	echo "     =====     END LOG     =====     "
fi

