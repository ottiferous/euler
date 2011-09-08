#	=============
#	Timer Wrapper
#	=============
echo "Solved Problems Runtime (fightbox)"
echo "========================="
echo ""
echo "Times listed for individual programs are in seconds - unless otherwise noted"
echo ""
echo "All times are derived from the built-in _profile_ method and the results stripped of extra information to make this pretty view"
echo ""
echo "Competing with [Zolrath](https://github.com/zolrath/Project-Clojuler)"
echo ""
echo "========================="

for each in *.py
do
	script=$(echo "$each" | cut -d "." -f1)
	echo -en "- *$script*\t--\t"
	line=`python -m profile $each | grep CPU`
	line=$(echo "$line" | cut -d " " -f 14)
	echo -e "*$line*"
	if [ `$each % 10` -eq 0 ]; then
		echo ""
	fi 
done
