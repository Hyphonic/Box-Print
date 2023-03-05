class Box:
    def __init__(self, Text):
        self.Text = Text
        self.Box = []
        self.Longest = max([len(Line) for Line in self.Text])

        # All The Box Types

        if type(self.Text) == str: # Single Line
            self.Box.append('╭' + '─' * (len(self.Text) + 2) + '╮')
            self.Box.append('│ ' + self.Text + ' ' * (len(self.Text) - len(self.Text)) + ' │')
            self.Box.append('╰' + '─' * (len(self.Text) + 2) + '╯')

        else: # Multiple Lines
            self.Box.append('╭' + '─' * (self.Longest + 2) + '╮')
            for Line in self.Text:
                if '<sep>' in Line.lower():
                    self.Box.append('├' + '─' * (self.Longest + 2) + '┤')
                else:
                    self.Box.append('│ ' + Line + ' ' * (self.Longest - len(Line)) + ' │')
            self.Box.append('╰' + '─' * (self.Longest + 2) + '╯')

        for Line in self.Box:
            print(Line)
