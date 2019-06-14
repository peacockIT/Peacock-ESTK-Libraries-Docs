Peacock PPRO BpmSlicer
----------------------

.. figure:: ../../modules/ppro_bpmslicer/images/BpmSlicer.png
    :align: right
    :figwidth: 350px

    Premiere Pro BpmSlicer.

A manual for the Premiere Pro extension

This extension is designed for creatively making music videos by developing a special midiclip along with your music production that helps you later in the video editing process.

Primarily this extension is made for music producers who are familiar with midi and the bpm value of a song.

Nevertheless you are not into music production and don't know how to create midiclips you can still use the other functionallity of this extension.

But you need to take a deeper look at the Preparations_.

Here you can find the |Premiere_Scripting_Guide|.

.. |Premiere_Scripting_Guide| raw:: html

   <a href="https://premiere-scripting-guide.readthedocs.io/" target="_blank">Premiere Scripting Guide</a>


---------

.. contents:: Table of Contents

---------

.. _Installation:

************
Installation
************


.. _Download the extension (.zxp file):

Download the extension (.zxp file)
==================================
When you download the extension, it comes as a zxp file to your computer's Downloads folder.
Enter any passwords, or accept any notices your computer’s operating system presents.

.. _Extension Install Utility:

Extension Install Utility
=========================
If you were unable to install your extension using the Creative Cloud desktop app,
please follow the instructions below to use an extension install utility.
In addition to Adobe's Manage Extensions utility there are various third party utilites
available that work with Adobe .zxp files, such as Anastasiy’s Extension Manager or |ZXPInstaller|.

Open the Extension Install Utility.
If you don’t have it on your computer, below are download links for alternative utilities.
Once downloaded and installed, use an extension install utility to install your .zxp files.

- Manage Extensions utility
- Anastasiy’s Extension Manager
- |ZXPInstaller|

After selecting either the Mac or Windows version of your chosen Extension Install Utility,
download it to your computer and follow the installation instructions from the installer,
which should be in your Downloads folder.

Install your extension from Adobe Exchange by selecting File > Install extension or
following the instructions within the install utility and selecting the extension
from within your computer’s Downloads folder.

Do not use Adobe Extension Manager for CC2015 or later compatible Adobe apps.
It is no longer supported and may create install issues. Use a third party utility
for extension installation, such as those mentioned above for installation,
if installation via the Creative Cloud desktop app is not successful.

.. |ZXPInstaller| raw:: html

   <a href="https://zxpinstaller.com/" target="_blank">ZXPInstaller</a>


.. _ExMan Command Line Tool:

ExMan Command Line Tool
=========================

You can even go a step further and use the command line tool |ExManCmd|.

1. Copy the ZXP package to ExMan_root. Let’s call it myextension.zxp.

2. Close any Adobe applications that are compatible with the Extension.

3. In a command shell (Mac OS Terminal or Windows Command Prompt), go to the ExMan_root folder and run this command for your extension:

  - In Mac OS: ``./Contents/MacOS/ExManCmd ––install myextension.zxp``
  - In Windows: ``ExManCmd.exe /install myextension.zxp``

    .. Note:: Currently, ExManCmd does not support encrypted extensions for enterprise use cases.

4. Check Where to Find it - Follow the instructions in the “Where to find it” section on the detail page. Some extensions may require you to carry out further steps to install.

This should install the add-on. You can verify the installation with this command:

- In Mac OS: ``./Contents/MacOS/ExManCmd ––list all``
- In Windows: ``ExManCmd.exe /list all``

.. |ExManCmd| raw:: html

   <a href="https://partners.adobe.com/exchangeprogram/creativecloud/support/exman-com-line-tool.html" target="_blank">ExManCmd</a>


.. _Where to Find it:

Where to Find it
================
After the installation you can find the extension placed in the extension folder.

- Windows: ``C:\Program Files (x86)\Common Files\Adobe\CEP\extensions``
- Mac: ``/Library/Application Support/Adobe/CEP/extensions``

**Resources:**

-  |adobeexchange_install_instructions|

.. |adobeexchange_install_instructions| raw:: html

   <a href="https://www.adobeexchange.com/creativecloud/install-instructions.20513.html" target="_blank">https://www.adobeexchange.com/creativecloud/install-instructions.20513.html</a>





---------

.. _Preparations:

************
Preparations
************

Before you can take full advantage of the functionality of the BpmSlicer you need to prepare your footage as follows.



.. _Song preparation:

Song preparation
================
You have to ensure that the following two conditions are met:

- You need to know the exact bpm value of the song you want to work with and set this value in the Bpm_ input field.

- You need to make sure that the 1 beat of the song sits exactly at the 0 point in time.

Some songs may not have an intro that fits the bpm rate of the actual song, then you
need to find the first beat and place it accordingly.

If you have the exact bpm rate of the song then it won't be too difficult to make it fit.



.. _Preparing the midi clip:

Preparing the midi clip
=======================

Please make sure that the midinotes in the midi file are placed in the range between C3 - B3, otherwise the notes won't be recognized.

.. figure:: ../../modules/ppro_bpmslicer/images/MidinoteRange.png
    :align: center

    Midinote range

.. code-block:: text

    C3  ->  videotrack 1
    C#3 ->  videotrack 2
    D3  ->  videotrack 3
    D#3 ->  videotrack 4
    ... ->  ...
    B3  ->  videotrack 12

.. Note:: The notes of C3 are placed onto videotrack 1, the notes of C#3 onto videotrack 2 and so on.



.. _Preparing your footage:

Preparing your footage
======================

If there is no BpmSlicer folder structure already you can create one by clicking the `Create folders`_ Button.

The next step is to put all your footage you want to be placed into the active sequence, according to the notes in the midi file,
into the ``1 source`` folder and assign the appropriate prefix for each footage item.

Make sure the prefix is a number between 1 - 12 and make sure there is a white space between the prefix number and the footage name.

The next thing you want to make sure is that you add as much videotracks to the active sequence as your highest assigned prefix is.

In the following example the highest assigned prefix is 4, so you need to make sure there are at least 4 videotracks available::

    BpmSlicer
        1 source
            1 VideoClip2.mov
            2 LensFlare2.mov
            3 Transition_1.mov
            4 PaperTexture_9.png
            4 PaperTexture_1.mov

As you notice in the example it's possible to assign the same prefix to as many footage items as you like.

If you assign the same prefix to more then one footage items, this function selects a random footage item each time it finds a midi note for the appropriate videotrack.



---------

.. _Functionality:

*************
Functionality
*************



.. _?:

?
===
Here you can find a short description for all functions of this extension.



.. _Bpm:

Bpm
===
Set the bpm rate of the song you want to edit your videos to.



.. _Bars:

Bars
====
Set bars in order to determine how many markers are created when creating markers.



.. _Create folders:

Create folders
==============
Creates the BpmSlicer folder structure::

    BpmSlicer
        1 source
        2 subclips



.. _Clips and markers from midi:

Clips and markers from midi
===========================

Before you can perform this function you need to refer to the chapter Preparations_ and make sure all conditions are met.

This function performs the following actions:

- Reads a midi file and interprets all midi notes in the range of C3 - B3.

- Creates a marker for each note-on event in the active sequence.

- Creates subclips and moves them into the ``1 subclips`` folder. See paragraph `Subclips with random starttime`_ to understand how the starttime is randomly set.

- Places footage that is arranged in the BpmSlicer ``1 source`` folder onto the appropriate videotrack of the active sequence.



.. _Clips and markers from txt:

Clips and markers from txt
==========================
Basically this function does the same thing as the function `Clips and markers from midi`_
except that a pre converted txt file is the source with all midi note informations included.

To create such a txt file that contains all required midi note information you need to
use the external application `Midiconverter (external)`_.



.. _Subclips with random starttime:

Subclips with random starttime
==============================
If a subclip is created it matches the duration of the appropriate midi note.

Note that the start time of the source footage is randomly selected but it is ensured that
the out points of the subclips are still inside the duration of the source footage.

.. code-block:: javascript
    :caption: Random starttime.

    startTime = ((sourceFootageDur - (2*midiNoteDur)) * Math.random()) + midiNoteDur;
    endTime = startTime + midiNoteDur;``



.. _Create subclips:

Create subclips
===============

This function considers all markers in the active sequence and places random clips from
the ``1 source`` folder onto videotrack 1 so that between each marker sits a subclip.

.. figure:: ../../modules/ppro_bpmslicer/images/BpmSlicer_createSubclips2.png
    :align: center
    :figwidth: 200px

    The **1 source** folder

In this case the assigned prefixes that were discussed in chapter `Preparing your footage`_
are immaterial.

.. figure:: ../../modules/ppro_bpmslicer/images/BpmSlicer_createSubclips.png
    :align: center

    Random clips from the **1 source** folder placed in the sequence

The starttime of the subclip is randomly set and it is made sure that the out point of
the subclip is inside the duration of the source footage.

.. code-block:: javascript
    :caption: Random starttime.

    startTimeSeconds = ((projectItemDur - (2*duration)) * Math.random()) + duration;
    endTimeSeconds = startTimeSeconds + duration;



.. _Sequence markers:

Sequence markers
================

There are two ways to create markers with the adjusted bpm- and bars-value:

- If one clip is selected the markers will be placed in the range of the clips in and out point.

- If there are more then one clips selected, the minimum in point and the maximum out point is considered.

If the in and outpoints of the sequence are set and no clip is selected,
then the markers will be created inside the time range of the sequences in and out points.



.. _Clip markers:

Clip markers
============

To create markers on one or more clips you need to place the clips into
the ``1 source`` folder and give it the prefix '0 ' (e.g. ``0 video.mov``).

If you then press the ``clip markers`` button, clip markers will be created according
to the adjusted ``Bpm`` and ``Bars`` value for the duration of the whole clip.



.. _Quantize sequence markers:

Quantize sequence markers
=========================
The sequence markers of the active sequence will be quantized to the sequences framerate.



.. _Export frames for markers:

Export frames for markers
=========================
Exports PNG images for each frame a marker is placed.



.. _Randomize selection:

Randomize selection
===================
Actually this is a randomized deselector.

You make a selection of clips and/or transitions and this function randomly deselct items from your selection.



.. _Change blendmode:

Change blendmode
================

.. figure:: ../../modules/ppro_bpmslicer/images/BpmSlicer_changeBlendmode.png
    :align: right
    :figwidth: 250px

    Change blendmode

You can select one or more blendmodes and apply them to the selected clips in the active sequence.

If you have more then one blendmodes selected, a random blendmode out of your blendmode
selection is assigned to the selection of clips in your active sequence.


---------

.. _Midiconverter (external):

************************
Midiconverter (external)
************************



.. _Midi converter button:

Midi converter button
=====================

The Midi converter interprets 12 note values in the range of C3 - B3.

.. figure:: ../../modules/ppro_bpmslicer/images/MidinoteRange.png
    :align: center
    :figwidth: 500px

    Midinote range

Please make sure that the midinotes are placed in exactly that range, otherwise the notes won't be recognized.

The chosen .mid file is converted to a .txt file with a assigned videotrack a note-on and note-off
value and a velocity value that can be imported by the Premiere Pro extension ``BpmSlicer``.
e.g.::

    1  0    2.5  0.5
    2  2.5  3.4  1.0



.. _Bpm editor:

Bpm editor
==========

Before the midi clip is converted, a tempo event with the given ``bpm`` rate is added to the midi clip.

If the midi clip has a tempo event already and you want to use it instead of a new one, set the bpm value to ``-1``.

If the bpm editor is empty the default bpm value of 120 is used.



.. _Fps editor:

Fps editor
==========
The fps value (Frames per seconds) is only needed if you want to use the clipboard to copy keyframes
directly onto one of After Effects layer properties.

With help of the fps value the time of the midi note-on values can be transformed to frame values.



.. _Clipboard:

Clipboard
=========
The velocity values of all midi note-on messages are mapped to the range of 0.0 - 1.0 and
copied to the systems clipboard so that you can simply paste the values as keyframes
onto a selected ``expression slider`` property in After Effects.

A ``expression slider`` with those keyframes can then be used to manipulate different properties and effects.



---------

.. _Troubleshooting:

***************
Troubleshooting
***************

.. figure:: ../../modules/ppro_bpmslicer/images/BpmVersionNumberInManifest.png
    :align: center

    Troubleshooting


.. Error::
   Installation failed because a newer version of the extension is installed.

   **Solution:** Change the ExtensionBundleVersion and the Extension version in the manifest.xml to a higher number then before.
   Then create a new .zxp file with ``ZXPSignCmd``.

   **Note:** This solution works only for the developer who has the source project files available, not if you only have the ``BpmSlicer.zxp`` file.



.. _Other BpmSlicer data pathes:

Other BpmSlicer data pathes
===========================

Other pathes that might help include BpmSlicer data

- Win: ``C:\Users\USERNAME\AppData\Local\Temp``
- Mac: ``/Users/USERNAME/Library/Logs/CSXS``
- ``/Users/USERNAME/Library/Application Support/Adobe/Extension Manager CC/Log/ExManCoreLibrary.log``
- ``/Users/USERNAME/Library/Preferences/com.Adobe.Premiere Pro.11.0.plist``
- ``/Users/USERNAME/Library/Preferences/com.Adobe.Premiere Pro.12.0.plist``


---------

.. _Development:

***********
Development
***********
In this section you can find some useful information about the development of a CEP HTML Extensions.
Please ignore this section if you're not a developer.


|CEP_8_0_HTML_Extension_Cookbook|
    |Debugging_Unsigned_Extensions|

    You can bypass the check for extension signatures by editing the CSXS preference properties file, located at:

      - Win: regedit > ``HKEY_CURRENT_USER/Software/Adobe/CSXS.8``, then add a new entry PlayerDebugMode of type "string" with the value of "1".
      - Mac: In the terminal, type: ``defaults write com.adobe.CSXS.8 PlayerDebugMode 1`` (The plist is also located at ``/Users/<username>/Library/Preferences/com.adobe.CSXS.8.plist``)



.. |CEP_8_0_HTML_Extension_Cookbook| raw:: html

   <a href="https://github.com/Adobe-CEP/CEP-Resources/blob/master/CEP_8.x/Documentation/CEP%208.0%20HTML%20Extension%20Cookbook.md" target="_blank">CEP 8.0 HTML Extension Cookbook</a>

.. |Debugging_Unsigned_Extensions| raw:: html

   <a href="https://github.com/Adobe-CEP/CEP-Resources/blob/master/CEP_8.x/Documentation/CEP%208.0%20HTML%20Extension%20Cookbook.md#debugging-unsigned-extensions" target="_blank">Debugging Unsigned Extensions</a>


.. _Packaging and Signing Adobe Extensions:

Packaging and Signing Adobe Extensions
======================================

This documentation of the packaging and signing procedure is based on |Packaging_and_Signing_Adobe_Extensions| pdf reference.


1. Download the the ZXPSignCMD tool from either |ZXPSignCMD_Git| or |ZXPSignCMD_Adobe|.

2. If you already have a certificate, you can use that. Otherwise, begin by by creating a self-signed certificate (`Create a self-signed certificate`_)::

    ./ZXPSignCmd -selfSignedCert US NY MyCompany MyCommonName abc123 MyCert.p12

3. This generates a file named ``MyCert.p12`` in the current folder. You can use this certificate to sign your extension (`Create a signed package`_)::

    ./ZXPSignCmd -sign myExtProject myExtension.zxp MyCert.p12 abc123


.. _Create a signed package:

-----------------------
Create a signed package
-----------------------

.. code-block:: bash

    ZXPSignCmd -sign <inputDir> <outputZxp> <p12> <p12Password> [options]

================  ==========================================================================================
   Inputs         Output
================  ==========================================================================================
``inputDir``      The path to the folder containing the source files to package.
``outputZxp``     The path and file name for the ZXP package.
``p12``           The signing certificate; see “How signing works” on page 5.
``p12Password``   The password for the certificate.
``options``       -tsa <timestampURL> The timestamp server. For example: https://timestamp.geotrust.com/tsa
================  ==========================================================================================


.. _Verify a ZXP package:

---------------------
Verify a ZXP package:
---------------------

.. code-block:: bash

    ZXPSignCmd -verify <zxp>|<extensionRootDir> [options]

+----------------------+-----------------------------------------------------------------------------------------------------------------------+
| Arguments            | Description                                                                                                           |
+======================+=======================================================================================================================+
| ``zxp``              | The path and file name for the ZXP package.                                                                           |
+----------------------+-----------------------------------------------------------------------------------------------------------------------+
| ``extensionRootDir`` | The path to the folder containing the deployed ZXP.                                                                   |
+----------------------+-----------------------------------------------------------------------------------------------------------------------+
| ``options``          | - ``-certinfo``                                                                                                       |
|                      | - If supplied, prints information about the certificate, including timestamp and revocation information.              |
|                      +-----------------------------------------------------------------------------------------------------------------------+
|                      | - ``-skipOnlineRevocationChecks``                                                                                     |
|                      | - If supplied, skips online checks for certificate revocation when -certinfo is set.                                  |
|                      +-------------------------------------+---------------------------------------------------------------------------------+
|                      | - ``-addCerts <cert1> <cert2> ...``                                                                                   |
|                      | - If supplied, verifes the certificate chain and assesses whether the supplied DER-encoded certificates are included. |
+----------------------+-------------------------------------+---------------------------------------------------------------------------------+


.. _Create a self-signed certificate:

--------------------------------
Create a self-signed certificate
--------------------------------

.. code-block:: bash

    ZXPSignCmd -selfSignedCert <countryCode> <stateOrProvince> <organization> <commonName> <password> <outputPath.p12> [options]

+-------------------------+-------------------------------------------------------------------------------------------------+
| Arguments               | Description                                                                                     |
+=========================+=================================================================================================+
| - ``countryCode``       | The certificate identifying information.                                                        |
| - ``stateOrProvince``   |                                                                                                 |
| - ``organization``      |                                                                                                 |
| - ``commonName``        |                                                                                                 |
+-------------------------+-------------------------------------------------------------------------------------------------+
| - ``password``          | The password for the new certificate.                                                           |
+-------------------------+-------------------------------------------------------------------------------------------------+
| - ``outputPath.p12``    | The path and file name for the new certificate.                                                 |
+-------------------------+-------------------------------------------------------------------------------------------------+
| - ``options``           | - ``-locality <code>``                                                                          |
|                         | - If supplied, the locale code to associate with this certificate.                              |
|                         +-------------------------------------------------------------------------------------------------+
|                         | - ``-orgUnit <name>``                                                                           |
|                         | - If supplied, an organizational unit to associate with this certificate.                       |
|                         +-------------------------------------------------------------------------------------------------+
|                         | - ``-email <addr>``                                                                             |
|                         | - If supplied, an email address to associate with this certificate.                             |
|                         +-------------------------------------------------------------------------------------------------+
|                         | - ``-validityDays <num>``                                                                       |
|                         | - If supplied, a number of days from the current date-time that this certificate remains valid. |
+-------------------------+-------------------------------------------------------------------------------------------------+



.. |Packaging_and_Signing_Adobe_Extensions| raw:: html

   <a href="https://wwwimages2.adobe.com/content/dam/acom/en/devnet/creativesuite/pdfs/SigningTechNote_CC.pdf" target="_blank">this</a>

.. |ZXPSignCMD_Git| raw:: html

   <a href="https://github.com/Adobe-CEP/CEP-Resources/tree/master/ZXPSignCMD" target="_blank">here</a>

.. |ZXPSignCMD_Adobe| raw:: html

   <a href="https://labs.adobe.com/downloads/extensionbuilder3.html" target="_blank">here</a>





