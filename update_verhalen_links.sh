#!/bin/bash
# Run from the forty repo root: bash update_verhalen_links.sh
FILE="verhalen/index.html"

# Update links from old forty.nl to new paths
sed -i '' 's|https://www.forty.nl/verhalen/waar-switcht-je-klant-van-weg-vier-vragen-die-elke-startup-en-propositieteam-moet-stellen|/forty/verhalen/waar-switcht-je-klant-van-weg/|g' "$FILE"
sed -i '' 's|https://www.forty.nl/verhalen/waarom-klanten-echt-overstappen---en-wat-jij-daarvan-kunt-leren|/forty/verhalen/waarom-klanten-echt-overstappen/|g' "$FILE"
sed -i '' 's|https://www.forty.nl/verhalen/waarom-jouw-klant-niet-kiest-voor-winst-maar-om-verlies-te-vermijden|/forty/verhalen/waarom-jouw-klant-niet-kiest-voor-winst/|g' "$FILE"
sed -i '' 's|https://www.forty.nl/verhalen/investeren-in-impact-achter-de-schermen-met-thijs-gitmans-van-shift-invest|/forty/verhalen/impact-investor-shift-invest/|g' "$FILE"
sed -i '' 's|https://www.forty.nl/verhalen/groei-zonder-groeipijn|/forty/verhalen/groei-zonder-groeipijn/|g' "$FILE"
sed -i '' 's|https://www.forty.nl/verhalen/fake-door-testing-weten-wat-je-doelgroep-doet|/forty/verhalen/fake-door-testing/|g' "$FILE"
sed -i '' 's|https://www.forty.nl/verhalen/hoe-bamboi-de-markt-voor-duurzaam-toiletpapier-wil-veranderen---een-zebra-show-interview|/forty/verhalen/bamboi-zebra-show/|g' "$FILE"
sed -i '' 's|https://www.forty.nl/verhalen/het-opstellen-van-aannames|/forty/verhalen/behavioral-design-principes/|g' "$FILE"
sed -i '' 's|https://www.forty.nl/verhalen/7-behavioral-design-principes-voor-startups-en-propositieteams|/forty/verhalen/behavioral-design-principes/|g' "$FILE"
sed -i '' 's|https://www.forty.nl/verhalen/kleinste-probleem-grootste-frustratie|/forty/verhalen/kies-en-ontwerp-je-experiment/|g' "$FILE"
sed -i '' 's|https://www.forty.nl/verhalen/kies-en-ontwerp-je-experiment|/forty/verhalen/kies-en-ontwerp-je-experiment/|g' "$FILE"

echo "Done! Links updated in $FILE"
echo "Verify with: grep 'forty.nl/verhalen' $FILE"
