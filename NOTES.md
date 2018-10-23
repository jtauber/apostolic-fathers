
* XML files from Perseus/OGL are in `raw-ogl-lake`
* edit `scripts/process-perseus.py` with filename and run,
  redirecting result to `structured/{}_OGL.txt`

* copy-paste from Logos to `logos/{}.txt`
* edit `scripts/process-logos.py` with new filename and run,
  redirecting result to `structured/{}_LOGOS.txt`
* remove blank sections from ``{}_LOGOS.txt` manually and
  fix up front and end matter

* edit `WORK` in `scripts/merge.py`
* run and redirect to `comparison/{}_COMPARE_ORIG.txt`
* fix lacunae/dittography in CCEL, OGL, and Logos and
  re-run merge until done

* give `{}_COMPARE_ORIG.txt` to Seumas
* copy `{}_COMPARE_ORIG.txt` to `{}_COMPARE_JT1.txt`

* correct `{}_COMPARE_JT1.txt` against the images of the printed
  Lake on Internet Archive (the same ones used for the OGL scan)

* save back Seumas's first corrections to `{}_COMPARE_SM1.txt`
* edit `scripts/compare_JT_SM.py` to reference these files
* generate first comparison and save as `{}_COMPARE_JT1vsSM1.txt`
* share with Seumas and each make another round of corrections

* repeat until a single text is converged on

* use `scripts/extract.py` to extract corrected text to
  `structured/{}_CORRECTED.txt`
* edit result to remove empty verses and change `~` to space