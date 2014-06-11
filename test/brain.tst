#!/bin/bash
# Test the brain functionality

echo brian list
rs brain list

echo
echo brain import xxx
rs brain import xxx

echo
echo brain import $HOME/Documents/MyBook/Public/ShrinkingWorld/Pricing
rs brain import $HOME/Documents/MyBook/Public/ShrinkingWorld/Pricing

echo
echo brain show Public/ShrinkingWorld/Pricing
rs   brain show Public/ShrinkingWorld/Pricing

echo '-------------------------------------------'
echo 'Errors'
echo
echo brain import
rs brain import


echo
echo brain xxx
rs brain xxx

echo
echo brain
rs brain

