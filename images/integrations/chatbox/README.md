# ChatBox Integration Screenshots Guide

This document describes all required screenshots for the ChatBox integration documentation.

## Overview

- **Total Screenshots Required**: 5
- **Image Format**: PNG (recommended) or JPG
- **Naming Convention**: Kebab-case (lowercase with hyphens)
- **Image Quality**: High resolution, clear and readable text
- **Language**: Chinese UI preferred, with English UI acceptable

## Required Screenshots

### 1. main-interface.png
**Description**: ChatBox configuration wizard shown on first launch  
**Content**:
- Full ChatBox application window with configuration dialog
- "使用自己的 API Key 或本地模型" button highlighted with red border
- Left sidebar showing example conversations
- Clean, welcome/setup interface

**Dimensions**: Recommended 1200x800px or higher  
**Usage**: Step 1 - Launching ChatBox and Starting Configuration

**Current Status**: ✅ Image captures the initial setup wizard perfectly

---

### 2. settings-page.png
**Description**: ChatBox settings page showing AI Provider selection  
**Content**:
- Settings page open
- AI Provider or AI Model Provider dropdown visible
- OpenAI API option visible in dropdown or selected
- Clear view of settings interface

**Dimensions**: Recommended 1200x800px or higher  
**Usage**: Step 2.1 - Selecting AI Model Provider

---

### 3. api-config.png
**Description**: API configuration fields showing API Key and API Host  
**Content**:
- API Key input field (can show placeholder or masked value)
- API Host or API Domain input field showing `https://api.apimart.ai`
- Clear labels for both fields
- Save or Apply button visible (if applicable)

**Dimensions**: Recommended 1000x600px or higher  
**Usage**: Step 2.2 - Configuring API Information

**Important Notes**:
- Do NOT show real API keys in screenshot
- Use placeholder like `sk-xxxxxxxxxxxxxxxxxxxx` or mask the key
- Ensure `https://api.apimart.ai` is clearly visible in API Host field

---

### 4. model-selection.png
**Description**: Model selection dropdown showing available models  
**Content**:
- Model dropdown menu open or expanded
- List of available models visible, including:
  - gpt-4o or gpt-4o-mini
  - Claude models (optional)
  - Other supported models
- Selected model highlighted (optional)

**Dimensions**: Recommended 800x600px or higher  
**Usage**: Step 2.3 - Selecting Model

**Alternative**: If ChatBox requires manual model name input, show the model input field with a model name typed in (e.g., `gpt-4o-mini`)

---

### 5. chat-interface.png
**Description**: ChatBox chat interface with active conversation  
**Content**:
- Active chat session with at least 2-3 message exchanges
- User messages and AI responses visible
- Clean, readable conversation flow
- Message input box at bottom
- Send button visible

**Dimensions**: Recommended 1200x800px or higher  
**Usage**: Step 3 - Start Using & Chat Interface demonstration

**Sample Conversation Ideas**:
- Simple greeting exchange
- Question about ChatBox features
- Code-related query and response
- Any topic that demonstrates the chat functionality

---

## Screenshot Capture Guidelines

### General Requirements

1. **Clean Interface**
   - Remove personal information (API keys, usernames, emails)
   - Clear any sensitive data from chat history
   - Use generic or sample data

2. **Image Quality**
   - High resolution (at least 1920x1080 native display)
   - No blur or distortion
   - Text must be clearly readable
   - Proper lighting/contrast

3. **Consistent Style**
   - All screenshots should be from the same ChatBox version
   - Consistent theme (light or dark mode)
   - Consistent window size where possible

4. **Language**
   - Chinese UI is preferred (matches target audience)
   - English UI is acceptable
   - Keep UI language consistent across all screenshots

### Technical Requirements

- **Format**: PNG (preferred for UI screenshots)
- **Color Mode**: RGB
- **Compression**: Moderate (balance file size and quality)
- **Max File Size**: 500KB per image (compress if needed)

### Platform-Specific Notes

- **Windows**: Use built-in Snipping Tool or Snip & Sketch
- **macOS**: Use Cmd+Shift+4 for area selection
- **Linux**: Use GNOME Screenshot or similar tools

## File Naming Convention

All files must use lowercase with hyphens:

✅ Correct:
- `main-interface.png`
- `api-config.png`
- `model-selection.png`

❌ Incorrect:
- `MainInterface.png`
- `api_config.png`
- `ModelSelection.jpg`

## Priority Order

If you can only provide some screenshots initially, prioritize in this order:

1. **High Priority** (Essential for setup):
   - `settings-page.png` - Shows how to access configuration
   - `api-config.png` - Shows critical API settings
   - `model-selection.png` - Shows how to select models

2. **Medium Priority** (Important for context):
   - `main-interface.png` - Shows starting point
   - `chat-interface.png` - Shows end result

3. **Low Priority** (Nice to have):
   - Additional screenshots for advanced features

## Post-Processing

Before submitting screenshots:

1. **Review Content**
   - Check for personal information
   - Verify API keys are masked/removed
   - Ensure no sensitive data visible

2. **Optimize Images**
   - Resize to recommended dimensions if too large
   - Compress to reduce file size if needed
   - Maintain readable text quality

3. **Validate**
   - Open each image and verify clarity
   - Check file names match convention
   - Confirm file formats are correct

## Notes for Documentation Team

- All screenshots should accurately reflect the current ChatBox UI
- If ChatBox UI changes significantly, screenshots may need updating
- Screenshots should match the steps described in the documentation
- Consider creating annotated versions (with arrows/highlights) for complex steps if needed

---

**Last Updated**: 2025-11-12  
**ChatBox Version**: Latest (as of documentation creation)  
**Document Version**: 1.0

